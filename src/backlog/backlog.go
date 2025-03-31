package backlog

import (
	"challenge_sbpo_2025/order"
)

type Backlog struct {
	orders []order.Order
}

func NewBacklog() *Backlog {
	return &Backlog{}
}

func (backlog *Backlog) AddOrder(order order.Order) {
	backlog.orders = append(backlog.orders, order)
}

func (backlog *Backlog) GetOrders() []order.Order {
	return backlog.orders
}
