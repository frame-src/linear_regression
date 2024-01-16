NAME = linear_regression
CC = gcc
FLAGS = -Wall -Wextra -Werror

SDIR = src

SRC =	./src/main.c ./src/linear_regression/gradient_descent.c \
		./src/linear_regression/rss.c ./src/linear_regression/utils.c \

OBJ = $(SRC:.c=.o)

%.o: $(SDIR)%.c
	$(CC) $(FLAGS) $^ -c

$(NAME): $(OBJ)
	$(CC) $(FLAGS) $^ -o $(NAME)

all: $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re