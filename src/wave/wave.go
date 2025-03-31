package wave

import "challenge_sbpo_2025/order"

type Wave struct {
	orders      []order.Order
	lower_bound int
	upper_bound int
}

func NewWave(lower_bound int, upper_bound int) *Wave {
	return &Wave{lower_bound: lower_bound, upper_bound: upper_bound}
}

func (wave *Wave) AddOrder(order order.Order) {
	wave.orders = append(wave.orders, order)
}

func (wave *Wave) GetOrders() []order.Order {
	return wave.orders
}
