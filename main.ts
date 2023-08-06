Tinybit.CarCtrl(Tinybit.CarState.Car_Run)
Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 140)
basic.pause(1000)
Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinLeft, 90)
basic.pause(200)
Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Back, 100)
basic.pause(500)
Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
basic.forever(function () {
	
})
