package access

import (
	"challenge_sbpo_2025/item"
)

type Access struct {
	id    int
	itens []item.Item
}

func NewAddress(id int) *Access {
	return &Access{id: id}
}

func (address *Access) GetId() int {
	return address.id
}

func (address *Access) AddItem(item item.Item) {
	address.itens = append(address.itens, item)
}
