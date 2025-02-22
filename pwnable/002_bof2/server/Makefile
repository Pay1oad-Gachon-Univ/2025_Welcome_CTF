CC = gcc
CFLAGS = -fno-stack-protector -no-pie
TARGET = prob
SRC = prob.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)
