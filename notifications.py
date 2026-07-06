def check_notifications(old_jobs, new_jobs):
    """"Find new jobs by comparing old and new job lists."""

    new_notifications = []

    for new_job in new_jobs:
        for old_job in old_jobs:
            if new_job == old_job:
                break
            
        else:
            new_notifications.append(new_job)

    return new_notifications
