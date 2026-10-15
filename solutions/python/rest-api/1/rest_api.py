
"""Implement a REST API for tracking IOUs."""

import json


class RestAPI:
    """Manage users and their IOU balances."""

    def __init__(self, database=None):
        if database is None:
            database = {"users": []}
        self.database = database

    def get(self, url, payload=None):
        """Return requested user information as JSON."""
        if url != "/users":
            return json.dumps({})

        users = self.database["users"]

        if payload is None:
            selected_users = users
        else:
            request_data = json.loads(payload)
            requested_names = request_data.get("users", [])
            selected_users = [
                user for user in users
                if user["name"] in requested_names
            ]

        result = {
            "users": sorted(
                selected_users,
                key=lambda user: user["name"],
            )
        }

        return json.dumps(result)

    def post(self, url, payload):
        """Create a user or record an IOU."""
        request_data = json.loads(payload)

        if url == "/add":
            name = request_data["user"]

            for user in self.database["users"]:
                if user["name"] == name:
                    return json.dumps(user)

            new_user = {
                "name": name,
                "owes": {},
                "owed_by": {},
                "balance": 0.0,
            }

            self.database["users"].append(new_user)
            return json.dumps(new_user)

        if url == "/iou":
            lender_name = request_data["lender"]
            borrower_name = request_data["borrower"]
            amount = request_data["amount"]

            lender = self._find_user(lender_name)
            borrower = self._find_user(borrower_name)

            # Cancel any existing debt in the opposite direction.
            cancelled_amount = min(
                amount,
                lender["owes"].get(borrower_name, 0.0),
            )

            remaining_amount = amount - cancelled_amount
            remaining_debt = (
                lender["owes"].get(borrower_name, 0.0)
                - cancelled_amount
            )

            if remaining_debt:
                lender["owes"][borrower_name] = remaining_debt
                borrower["owed_by"][lender_name] = remaining_debt
            else:
                lender["owes"].pop(borrower_name, None)
                borrower["owed_by"].pop(lender_name, None)

            if remaining_amount:
                lender["owed_by"][borrower_name] = (
                    lender["owed_by"].get(borrower_name, 0.0)
                    + remaining_amount
                )
                borrower["owes"][lender_name] = (
                    borrower["owes"].get(lender_name, 0.0)
                    + remaining_amount
                )

            lender["balance"] += amount
            borrower["balance"] -= amount

            result = {
                "users": sorted(
                    [lender, borrower],
                    key=lambda user: user["name"],
                )
            }

            return json.dumps(result)

        return json.dumps({})

    def _find_user(self, name):
        """Find a user by name."""
        for user in self.database["users"]:
            if user["name"] == name:
                return user

        raise ValueError(f"User {name} not found")
