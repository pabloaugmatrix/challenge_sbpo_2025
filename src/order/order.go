package order

import (
	"challenge_sbpo_2025/item"
)

type Order struct {
	id    int
	itens []item.Item
}

func NewOrder(id int) *Order {
	return &Order{id: id}
}

func (order *Order) GetId() int {
	return order.id
}

func (order *Order) AddItem(item item.Item) {
	order.itens = append(order.itens, item)
}

func (order *Order) GetItens() []item.Item {
	return order.itens
}
