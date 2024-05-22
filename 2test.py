class HouseRabbit(Rabbit):
  shape = "house"

  def __init__(self, x, y):
    self.goto(x, y)

  def eat_feed(self):
    print("토끼가 사료를 먹습니다.")