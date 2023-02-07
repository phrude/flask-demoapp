.PHONY: clean

NAME = malware

help: ## Print this help message
	@grep -E '^[a-zA-Z._-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

build: malicious.cpp ## Build a malicious binary file
	g++ -o $(NAME) $<

clean: ## Clean a generated binary file
	rm -f $(NAME)

