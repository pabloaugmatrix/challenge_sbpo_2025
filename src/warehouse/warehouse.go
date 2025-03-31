package warehouse

import (
	"challenge_sbpo_2025/access"
	"challenge_sbpo_2025/backlog"
)

type Warehouse struct {
	backlog  backlog.Backlog
	accesses []access.Access
}

func NewWarehouse(backlog backlog.Backlog) *Warehouse {
	return &Warehouse{backlog: backlog}
}

func (warehouse *Warehouse) AddAccess(access access.Access) {
	warehouse.accesses = append(warehouse.accesses, access)
}
func (warehouse *Warehouse) GetAccesses(id int) []access.Access {
	return warehouse.accesses
}

func (warehouse *Warehouse) GetBacklog() backlog.Backlog {
	return warehouse.backlog
}
