import pinocchio as pin
from .path import *

def loadGo2() -> pin.RobotWrapper:
    robot = pin.RobotWrapper.BuildFromURDF(GO2_DESCRIPTION_URDF_PATH, [GO2_DESCRIPTION_PACKAGE_DIR], pin.JoinModelFreeFlyer())

    # Reference configurations
    pin.loadReferenceConfigurations(robot.model, GO2_DESCRIPTION_SRDF_PATH)

    return robot