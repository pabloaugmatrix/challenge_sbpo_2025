package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Uso: go run main.go <instance_000x.txt>")
		return
	}

	dataset_name := os.Args[1]
	dataset_path := "../data/input/" + dataset_name

	conteudo, err := os.ReadFile(dataset_path)
	if err != nil {
		fmt.Println("Erro ao ler dataset:", err)
		return
	}

	fmt.Printf("Conteudo do dataset %s:\n%s", string(dataset_name), string(conteudo))

}
