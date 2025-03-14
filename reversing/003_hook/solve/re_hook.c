#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <windows.h>

#define TOTAL_MESSAGES 500
#define SPECIAL_COUNT 33
#define SHIFT_VALUE 0x5A 
#define INTERVAL 100 

// 인코딩된 문자열 데이터
char randomBytes[] = {
    'd' ^ SHIFT_VALUE, 'e' ^ SHIFT_VALUE, 'c' ^ SHIFT_VALUE,
    '0' ^ SHIFT_VALUE, 'd' ^ SHIFT_VALUE, '1' ^ SHIFT_VALUE,
    'n' ^ SHIFT_VALUE, 'g' ^ SHIFT_VALUE, '_' ^ SHIFT_VALUE,
    'K' ^ SHIFT_VALUE, '3' ^ SHIFT_VALUE, 'y' ^ SHIFT_VALUE,
    '!' ^ SHIFT_VALUE, 's' ^ SHIFT_VALUE, '_' ^ SHIFT_VALUE,
    '<' ^ SHIFT_VALUE, 's' ^ SHIFT_VALUE, '3' ^ SHIFT_VALUE,
    'c' ^ SHIFT_VALUE, 'R' ^ SHIFT_VALUE, '3' ^ SHIFT_VALUE,
    't' ^ SHIFT_VALUE, '_' ^ SHIFT_VALUE, 'k' ^ SHIFT_VALUE,
    '3' ^ SHIFT_VALUE, 'y' ^ SHIFT_VALUE, '!' ^ SHIFT_VALUE,
    's' ^ SHIFT_VALUE, '_' ^ SHIFT_VALUE, 'A' ^ SHIFT_VALUE,
    'E' ^ SHIFT_VALUE, 'S' ^ SHIFT_VALUE, '>' ^ SHIFT_VALUE,
    '\0'
};

// 데이터 복호화 함수
void obscurePattern(char* output) {
    for (size_t index = 0; index < strlen(randomBytes); ++index) {
        output[index] = randomBytes[index] ^ SHIFT_VALUE; // 데이터 변환
    }
}

// 내용 변형 함수
void tweakBuffer(char* buffer, size_t length, char modifier) {
    for (size_t index = 0; index < length; ++index) {
        buffer[index] ^= modifier; // 버퍼 수정
    }
}

// 메시지 박스를 표시하는 스레드
DWORD WINAPI showWindowThread(LPVOID param) {
    char* messageBuffer = (char*)param;
    MessageBoxA(NULL, messageBuffer + 50, messageBuffer, MB_OK); // 메시지 박스 생성
    free(param); // 동적 메모리 해제
    return 0;
}

// 메시지 출력 함수
void initiateNotifications() {
    srand((unsigned int)time(NULL));
    int randomIndices[SPECIAL_COUNT];
    int totalCount = TOTAL_MESSAGES;

    // 무작위 인덱스 선택
    for (int index = 0; index < SPECIAL_COUNT; ++index) {
        int newIndex;
        int isDuplicate;

        do {
            newIndex = rand() % totalCount;
            isDuplicate = 0;

            for (int check = 0; check < index; ++check) {
                if (randomIndices[check] == newIndex) {
                    isDuplicate = 1; // 중복 인덱스 확인
                    break;
                }
            }
        } while (isDuplicate);

        randomIndices[index] = newIndex; // 선택된 인덱스 저장
    }

    // 암호화된 데이터 복호화
    char outputData[sizeof(randomBytes)];
    obscurePattern(outputData); // 데이터 복호화 호출

    // 메시지 박스 출력
    for (int index = 0; index < totalCount; ++index) {
        const char* title = "Standard Notification"; // 기본 제목
        char content[100] = "this is not the key..."; // 기본 내용

        for (int jndex = 0; jndex < SPECIAL_COUNT; ++jndex) {
            if (randomIndices[jndex] == index) {
                title = "Special Key"; // 특별 메시지 제목
                snprintf(content, sizeof(content), "key: %d. %c", jndex + 1, outputData[jndex]); // 내용 업데이트
                break;
            }
        }

        char* messageBuffer = (char*)malloc(150); // 메시지 버퍼 동적 할당
        snprintf(messageBuffer, 50, "%s", title); // 제목 저장
        snprintf(messageBuffer + 50, 100, "%s", content); // 내용 저장

        CreateThread(NULL, 0, showWindowThread, messageBuffer, 0, NULL); // 스레드 생성

        Sleep(INTERVAL); // 잠시 대기
    }
}

int main() {
    printf("Program is initializing...\n");
    initiateNotifications(); // 메시지 출력 함수 호출

    printf("All notifications have been displayed.\n");
    Sleep(5000); // 프로그램 종료 전 대기

    return 0;
}










