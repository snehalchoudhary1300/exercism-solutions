
"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the express or normal queue."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue, friend_name):
    """Return the index of the friend's name."""
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Insert a person at the given index."""
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove the specified person from the queue."""
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Count how many times a name appears in the queue."""
    return queue.count(person_name)


def remove_the_last_person(queue):
    """Remove and return the last person in the queue."""
    return queue.pop()


def sorted_names(queue):
    """Return a sorted copy of the queue."""
    return sorted(queue)
