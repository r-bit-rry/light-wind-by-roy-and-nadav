Tinybit.car_ctrl(Tinybit.CarState.CAR_RUN)
Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 140)
basic.pause(1000)
Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 90)
basic.pause(200)
Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_BACK, 100)
basic.pause(500)
Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)

def on_forever():
    pass
basic.forever(on_forever)
