import time
import ALMemoryKey
import FilesRW as Frw


def record_animation1(motion, memory, path, loop, filename):
    print "operate the robot..."
    l = 0
    isRecording = True
    csv_path = Frw.create_csv(path, filename)
    animation_list = []
    start = time.time()
    motion.setStiffnesses('Head', 0)
    motion.setStiffnesses('LArm', 0)
    motion.setStiffnesses('RArm', 0)
    while l < loop:
        if not isRecording:
            break
        l += 1
        print "loop:"
        print l
        save_data(memory, animation_list)
        time.sleep(0.15)
    end = time.time()
    print "recoding time: {} seconds.".format(end - start)
    Frw.save_result(animation_list, csv_path)
    return csv_path




def record_animation(motion, memory, path, loop, filename):
    """
    Record the motions of upper body for LOOP times
    :param loop: Recording times 
    :param path: path of directory to create csv file
    :param motion: ALMotion instance
    :param memory: ALMemory instance
    :return: Path of csv file
    """
    print "operate the robot..."
    l = 0
    csv_path = Frw.create_csv(path, filename)
    animation_list = []
    start = time.time()
    while l < loop:
        l += 1
        print "loop:"
        print l
        record = 0
        for joint in ALMemoryKey.UPPERBODY_TORQUE_KEY.keys():
            value = memory.getData(ALMemoryKey.UPPERBODY_TORQUE_KEY[joint])
            if value <= ALMemoryKey.ALMEMORY_TORQUE_THRESHOLD[joint]:
                motion.setStiffnesses(joint, 1)
            else:
                motion.setStiffnesses(joint, 0)
                record = 1
        time.sleep(0.2)
        if record != 1:
            print "recording data..."
            save_data(memory, animation_list)
    end = time.time()
    print "recoding time: {} seconds.".format(end - start)
    Frw.save_result(animation_list, csv_path)
    return csv_path


def load_animation(motion, path):
    """
    Load animation from csv file
    :param motion: motion ALProxy
    :param path: csv file path
    """
    print "Start loading animation recorded..."
    try:
        animation_lists, length = Frw.load_result(path)
    except Exception:
        motion.rest()
        return False
    else:
        names = Frw.fieldnames
        angles = []
        times = []
        single_time = []
        for i in range(1, length+1):
            t = round(0.2*i, 2)
            single_time.append(t)
        isAbsolute = True
        for name in names:
            angles.append(animation_lists[name])
            times.append(single_time)
        try:
            start = time.time()
            motion.angleInterpolation(names, angles, times, isAbsolute)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception :
            print "Nothing recorded!"
        print "finished"
        return True


def save_data(memory, data_list):
    """
    Save data from ALMemory as a dictionary to list
    :param memory: ALMemory instance
    :param data_list: list of data dictionaries
    """
    results = {}
    for joint in ALMemoryKey.UPPERBODY_POSITION_KEY.keys():
        results[joint] = memory.getData(ALMemoryKey.UPPERBODY_POSITION_KEY[joint])
    data_list.append(results)