CC = gcc
CFLAGS = -fno-stack-protector
TARGET = prob
SRC = prob.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)
