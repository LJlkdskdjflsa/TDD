""" Mars Rover (火星探索者號)
學習目標：The Rule of Three & Duplicate code
撰寫測試後
減少重複

任務：
您是透過將遙控飛行器傳送到地球表面來探索火星的團隊的一員。 開發一個API，將從地球傳送的命令轉換為漫遊者理解的指令。

要求：
將獲得漫遊者的初始起點（x，y）及其所面對的方向（N，S，E，W）。
漫遊者接收命令的字元陣列。
實現向前/向後移動漫遊者的命令（f，b）。
實現命令，使漫遊者左/右轉動（l，r）。
在邊緣實現包裝。 但要小心，行星就是球體。
在每次移動到新廣場之前實施障礙物檢測。 如果給定的命令序列遇到障礙物，漫遊者將移動到最後可能的點，中止序列並報告障礙物。

規則：TDD
在每個TDD週期後更改角色（驅動器、導航器）。
重構時沒有紅色相位。
小心邊緣情況和例外情況。 我們不能僅僅因為開發人員忽略了空指標就失去火星漫遊者。

完整練習題：https://kata-log.rocks/mars-rover-kata
"""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Rover:
    facing: str

    def turn(self, instruction: str):
        compass = ("N", "E", "S", "W")
        if instruction == "R":
            current = compass.index(self.facing)
            return replace(self, facing=compass[(current + 1) % 4])

        current = compass.index(self.facing)
        return replace(self, facing=compass[(current + 3) % 4])
