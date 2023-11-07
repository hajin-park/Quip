from copy import deepcopy
import numpy as np
import cv2 as cv
import itertools


def calc_bounding_rect(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_array = np.empty((0, 2), int)

    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)

        landmark_point = [np.array((landmark_x, landmark_y))]

        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv.boundingRect(landmark_array)

    return [x, y, x + w, y + h]


def calc_landmark_list(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []

    # Keypoint
    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        # landmark_z = landmark.z

        landmark_point.append([landmark_x, landmark_y])

    return landmark_point


def pre_process_landmark(landmark_list):
    temp_landmark_list = deepcopy(landmark_list)

    # Convert to relative coordinates
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]

        temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
        temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y

    # Convert to a one-dimensional list
    temp_landmark_list = list(itertools.chain.from_iterable(temp_landmark_list))

    # Normalization
    max_value = max(list(map(abs, temp_landmark_list)))

    def normalize_(n):
        return n / max_value

    temp_landmark_list = list(map(normalize_, temp_landmark_list))

    return temp_landmark_list


def draw_landmarks(image, landmark_point):
    if len(landmark_point) > 0:
        # Thumb
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[3]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[3]), tuple(landmark_point[4]), (255, 255, 255), 1)

        # Index finger
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[6]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[6]), tuple(landmark_point[7]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[7]), tuple(landmark_point[8]), (255, 255, 255), 1)

        # Middle finger
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[10]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[10]), tuple(landmark_point[11]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[11]), tuple(landmark_point[12]), (255, 255, 255), 1)

        # Ring finger
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[14]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[14]), tuple(landmark_point[15]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[15]), tuple(landmark_point[16]), (255, 255, 255), 1)

        # Little finger
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[18]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[18]), tuple(landmark_point[19]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[19]), tuple(landmark_point[20]), (255, 255, 255), 1)

        # Palm
        cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[0]), tuple(landmark_point[1]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[1]), tuple(landmark_point[2]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[2]), tuple(landmark_point[5]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[5]), tuple(landmark_point[9]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[9]), tuple(landmark_point[13]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[13]), tuple(landmark_point[17]), (255, 255, 255), 1)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]), (0, 0, 0), 3)
        cv.line(image, tuple(landmark_point[17]), tuple(landmark_point[0]), (255, 255, 255), 1)

    # Key Points
    for index, landmark in enumerate(landmark_point):
        if index == 0:  # 手首1
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 1:  # 手首2
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 2:  # 親指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 3:  # 親指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 4:  # 親指：指先
            cv.circle(image, (landmark[0], landmark[1]), 4, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 4, (0, 0, 0), 1)
        if index == 5:  # 人差指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 6:  # 人差指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 7:  # 人差指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 8:  # 人差指：指先
            cv.circle(image, (landmark[0], landmark[1]), 4, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 4, (0, 0, 0), 1)
        if index == 9:  # 中指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 10:  # 中指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 11:  # 中指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 12:  # 中指：指先
            cv.circle(image, (landmark[0], landmark[1]), 4, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 4, (0, 0, 0), 1)
        if index == 13:  # 薬指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 14:  # 薬指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 15:  # 薬指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 16:  # 薬指：指先
            cv.circle(image, (landmark[0], landmark[1]), 4, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 4, (0, 0, 0), 1)
        if index == 17:  # 小指：付け根
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 18:  # 小指：第2関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 19:  # 小指：第1関節
            cv.circle(image, (landmark[0], landmark[1]), 3, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 3, (0, 0, 0), 1)
        if index == 20:  # 小指：指先
            cv.circle(image, (landmark[0], landmark[1]), 4, (255, 255, 255), -1)
            cv.circle(image, (landmark[0], landmark[1]), 4, (0, 0, 0), 1)

    return image


def draw_bounding_rect(use_brect, image, brect):
    if use_brect:
        # Outer rectangle
        cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[3]), (0, 0, 0), 1)

    return image


def draw_info_text(image, brect, handedness, hand_sign_text):
    cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[1] - 22), (0, 0, 0), -1)

    # info_text = handedness.classification[0].label[0:]
    info_text = "N/A"
    if hand_sign_text != "":
        # info_text = info_text + ":" + hand_sign_text
        info_text = hand_sign_text
    cv.putText(
        image, info_text, (brect[0] + 5, brect[1] - 4), cv.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1, cv.LINE_AA
    )

    return image


def gesture_crop_dimensions(x, y, hand_crop, width, height):
    x_upper = int(x - hand_crop) if int(x - hand_crop) > 0 else 0
    y_upper = int(y - hand_crop * 2) if int(y - hand_crop * 2) > 0 else 0
    x_lower = int(x + hand_crop) if int(x + hand_crop) < width else width
    y_lower = int(y + hand_crop / 2) if int(y + hand_crop / 2) < height else height

    return x_upper, y_upper, x_lower, y_lower