from typing import List, Tuple


def main():
    history = {}

    def stage_1(arr: List) -> Tuple[int, int]:
        history
        buttons, prompt = arr[:-1], arr[-1]
        match prompt:
            case 1:
                result = (buttons[1], 1)
            case 2:
                result = (buttons[1], 1)
            case 3:
                result = (buttons[2], 2)
            case 4:
                result = (buttons[3], 3)

        history["stage_1"] = result[:]
        return result[0]

    def stage_2(arr: List) -> Tuple[int, int]:
        history
        buttons, prompt = arr[:-1], arr[-1]
        match prompt:
            case 1:
                idx = buttons.index(4)
                result = (buttons[idx], idx)
            case 2:
                idx = history["stage_1"][1]
                result = (buttons[idx], idx)
            case 3:
                result = (buttons[0], 0)
            case 4:
                idx = history["stage_1"][1]
                result = (buttons[idx], idx)

        history["stage_2"] = result[:]
        return result[0]

    def stage_3(arr: List) -> Tuple[int, int]:
        history
        buttons, prompt = arr[:-1], arr[-1]
        match prompt:
            case 1:
                idx = buttons.index(history["stage_2"][0])
                result = (buttons[idx], idx)
            case 2:
                idx = buttons.index(history["stage_1"][0])
                result = (buttons[idx], idx)
            case 3:
                result = (buttons[2], 2)
            case 4:
                idx = buttons.index(4)
                result = (buttons[idx], idx)

        history["stage_3"] = result[:]
        return result[0]

    def stage_4(arr: List) -> Tuple[int, int]:
        history
        buttons, prompt = arr[:-1], arr[-1]
        match prompt:
            case 1:
                idx = history["stage_1"][1]
                result = (buttons[idx], idx)
            case 2:
                result = (buttons[0], 0)
            case 3:
                idx = history["stage_2"][1]
                result = (buttons[idx], idx)
            case 4:
                idx = history["stage_2"][1]
                result = (buttons[idx], idx)

        history["stage_4"] = result[:]
        return result[0]

    def stage_5(arr: List) -> Tuple[int, int]:
        history
        buttons, prompt = arr[:-1], arr[-1]
        match prompt:
            case 1:
                idx = history["stage_1"][1]
                result = (buttons[idx], idx)
            case 2:
                idx = history["stage_2"][1]
                result = (buttons[idx], idx)
            case 3:
                idx = history["stage_3"][1]
                result = (buttons[idx], idx)
            case 4:
                idx = history["stage_4"][1]
                result = (buttons[idx], idx)

        history["stage_5"] = result[:]
        return result[0]

    # THIS IS THE SOLUTION !!1!
    def decipher(data: List[List[int]]) -> str:
        get_function = [stage_1, stage_2, stage_3, stage_4, stage_5]
        result = []
        for idx, arr in enumerate(data):
            result.append(str(get_function[idx](arr)))
        return "".join(result)

    def test():
        data_in = [[1, 3, 2, 4, 1], [3, 1, 2, 4, 3], [2, 3, 4, 1, 2], [2, 1, 4, 3, 1], [4, 1, 2, 3, 4]]
        pin = decipher(data_in)
        print(pin)

    # test()


if __name__ == "__main__":
    main()
