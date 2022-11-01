# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第18章
@Author  : Rey
@Time    : 2022-11-01 18:16:10
"""

class RoleStateMemento:
    def __init__(self, vitality, attach, defense) -> None:
        self.vitality = vitality
        self.attach = attach
        self.defense = defense


class GameRole:
    def __init__(self) -> None:
        self.vitality = 0
        self.attack = 0
        self.defense = 0

    def state_disply(self):
        print("角色当前状态:")
        print(f"体力: {self.vitality}")
        print(f"攻击力: {self.attack}")
        print(f"防御力: {self.defense}")
        print()

    def get_init_state(self):
        self.vitality = 100
        self.attack = 100
        self.defense = 100

    def fight(self):
        self.vitality = 0
        self.attack = 0
        self.defense = 0

    def save_state(self):
        return RoleStateMemento(self.vitality, self.attack, self.defense)

    def recovery_state(self, memento: RoleStateMemento):
        self.vitality = memento.vitality
        self.attach = memento.attach
        self.defense = memento.defense


class RoleStateCaretaker:
    def __init__(self) -> None:
        self.memento = None


if __name__ == '__main__':
    lixiaoyao = GameRole()
    lixiaoyao.get_init_state()
    lixiaoyao.state_disply()

    # 保存进度
    state_admin = RoleStateCaretaker()
    state_admin.memento = lixiaoyao.save_state()

    # 打boss
    lixiaoyao.fight()
    lixiaoyao.state_disply()

    # 恢复之前状态
    lixiaoyao.recovery_state(state_admin.memento)
    lixiaoyao.state_disply()
