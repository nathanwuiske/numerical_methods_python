import matplotlib.pyplot as plt

def sky_dive(mass = 80, height = 2500, height_open = 700, DT = 0.001, simLength = 200):
    velocity = 0
    numIterations = int(simLength/DT) + 1
    acceleration_due_to_gravity = -9.81
    weight = mass * acceleration_due_to_gravity
    projected_area = 28
    air_friction = -0.65 * projected_area *  velocity * abs(velocity)
    total_force = weight + air_friction
    acceleration = total_force / mass
    change_in_velocity = acceleration
    change_in_height = velocity
    t = 0
    timeLst = [0]
    heightLst = [height]
    speed = abs(velocity)
    speedLst = [speed]

    for i in range(1, numIterations):
        t = i * DT
        velocity = velocity + (change_in_velocity) * DT
        speed = abs(velocity)
        height = height + (change_in_height) * DT
        if height < 0:
            break
        timeLst.append(t)
        speedLst.append(speed)
        heightLst.append(height)
        if (height > height_open):
            projected_area = 0.4
        else:
            projected_area = 28
        air_friction = -0.65 * projected_area * velocity * abs(velocity)
        total_force = weight + air_friction
        acceleration = total_force / mass
        change_in_height = velocity
        change_in_velocity = acceleration

    plt.plot(timeLst, heightLst, 'ro')
    plt.xlabel('Time')
    plt.ylabel('height')
    plt.show()
    plt.plot(timeLst, speedLst, 'ro')
    plt.xlabel('Time')
    plt.ylabel('Speed')
    plt.show()

sky_dive()
