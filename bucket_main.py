import bucket_ui
##########################
goal_number = "4"
goal_bucket = "A"

max_a = 5
max_b = 3
##########################

bucket_a = 0
bucket_b = 0

def test_win():
    if goal_bucket == "A" and bucket_a == goal_number or goal_bucket == "B" and bucket_b == goal_number:
        pass

def update():
    global bucket_a
    bucket_ui.ba["state"] = "normal"
    bucket_ui.ba.delete(0, bucket_ui.END)
    bucket_ui.ba.insert(0, bucket_a)
    bucket_ui.ba["state"] = "disabled"

    global bucket_b
    bucket_ui.bb["state"] = "normal"
    bucket_ui.bb.delete(0, bucket_ui.END)
    bucket_ui.bb.insert(0, bucket_b)
    bucket_ui.bb["state"] = "disabled"

def fill_a():
    global bucket_a
    bucket_a = max_a
    update()

def empty_a():
    global bucket_a
    bucket_a = 0
    update()

def fill_b():
    global bucket_b
    bucket_b = max_b
    update()

def empty_b():
    global bucket_b
    bucket_b = 0
    update()

def a_to_b():
    global bucket_a
    global bucket_b
    old_b = bucket_b
    old_a = bucket_a
    bucket_b += bucket_a
    bucket_a = 0
    if bucket_b > max_b:
        bucket_a =  old_a - (max_b - old_b)
        bucket_b = max_b
    update()
    test_win()

def b_to_a():
    global bucket_a
    global bucket_b
    old_b = bucket_b
    old_a = bucket_a
    bucket_a += bucket_b
    bucket_b = 0
    if bucket_a > max_a:
        bucket_b = old_b - (max_a - old_a)
        bucket_a = max_a
    update()
    test_win()

