package item

type Item struct {
	id       int
	quantity int
}

func NewItem(id int, quantity int) *Item {
	return &Item{id: id, quantity: quantity}
}

func (item *Item) GetId() int {
	return item.id
}

func (item *Item) GetQuantity() int {
	return item.quantity
}
