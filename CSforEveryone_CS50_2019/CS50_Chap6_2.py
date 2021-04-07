"""
모두를 위한 컴퓨터 과학(CS50)
2021.04.07
Chapter 6. Data Structures 자료구조

"""


"""
5) 연결 리스트 : 시연

연결 리스트는 값을 추가할 때,
기존의 배열처럼 새로 전체의 메모리를 할당하고 다시 값을 지정해주지 않고
그저 malloc으로 새로운 값의 메모리만을 받아서, 리스트의 마지막 값과 연결해주면 된다.
유동적으로 프로그래밍할 수 있게된 것이다.

그러나 기존 배열의 장점이었던 임의 접근이 불가능해졌다.
리스트의 어떤 값에 접근하기 위해서는 리스트의 처음 요소부터 시작하여
모든 포인터를 따라가야만 한다.
그렇기 때문에 연결 리스트의 실행 시간은 기존의 배열의 실행 시간이었던 O(log n)에서 
요소의 개수만큼으로 늘어나 O(n)가 되었고
배열의 장점이었던 이진 탐색도 할 수 없어진다.



- 연결 리스트를 코드로 구현해보자.

#include <stdio.h>
#include <stdlib.h>

// 구조체 만들기.
typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    // 리스트 초기화.
    node *list = NULL;
    
    // 숫자 추가하기.
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next = NULL;
    list = n;
    
    // 숫자 추가하기.
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 2;
    n->next = NULL;
    list->next = n;
    
    // 숫자 추가하기.
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n;
    
    // 리스트 출력하기.
    for (node *tmp; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
    
    // 메모리 해제하기.
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list)
        list = tmp;
    }
}





6) 연결 리스트 : 트리

연결 리스트에 수직적인 개념을 도입해서 2차원적으로 생각해보자.

1  2  3  4  5  6  7 이라는 배열이 있을 때,

중간값(루트) : 4
왼쪽 : 2, 오른쪽 : 6
2의 왼쪽 : 1, 2의 오른쪽 : 3
6의 왼쪽 : 5, 6의 오른쪽 : 7 의 순서로 탐색한다.

4로부터 2, 6을 가리키는 두 개의 포인터
2로부터 1, 3
6으로부터 5, 7을 가리키는 두 개의 포인터를 가지게끔 node를 만들어보자.
left와 right가 될 것이다.

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;



하나의 노드는 두 개의 자식 노드를 가지고
어떤 노드에서든 왼쪽이 작고 오른쪽이 큰 구조를 띈다.
따라서 트리 구조는 재귀적인 이진 검색에 유리하다.



- 트리 구조에서 50을 찾아보자.
bool search(node *tree)
{
    // 빈 주소를 입력받으면 -> false 반환.
    if (tree = NULL)
    {
        return false;
    }
    
    // 트리의 숫자가 50보다 크다면 왼쪽 탐색.
    else if (50 < tree->number)
    {
        return search(tree->left);
    }
    
    // 트리의 숫자가 50보다 작다면 오른쪽 탐색.
    else if (50 > tree->number)
    {
        return search(tree->right)'
    }
    
    // 트리의 숫자가 50과 같다면 -> true 반환.
    else if (50 == tree->number)
    {
        return true;
    }
}



따라서 트리 구조에서의 이진 탐색은 O(log n)의 상한 시간을 갖게되고
트리 구조에 새로운 요소를 추가할 때도 동일하게 O(log n)의 상한을 가진다.





7) 해시 테이블

여러 명의 사람이 있을 때 그들의 이름표를 각각의 알파벳 상자에 넣어보자.
이 상자의 배열에는 A부터 Z까지 순서가 정해져있다. (26개)
이 해시 테이블은 각각의 알파벳 상자에 랜덤 접근할 수 있다.
그러나 하나의 상자에 여러개의 이름이 들어있을 때는
ex) H - Hermione, Harry, Hagrid
각각의 이름을 연결 리스트로 처리하여 가로로 확장시킬 수 있다.

만약 H로 시작하는 이름이 아주 많아지면 어떻게 해야할까 ?
Ha Hb, Hc, Hd ... Hx, Hy, Hz 로 새로운 상자를 만들어 이름을 넣거나
더 나아가서 Haa, Hab, Hac ... Hka, Hkb ... Hzy, Hzz 으로
26 * 26 * 26개의 상자를 만들어 넣을 수도 있을 것이다.

그렇게 된다면 모든 이름이 각각 하나의 상자에 들어가서
검색 시간이 O(1)로 줄어들 수도 있다.
그러나 H로 시작하는 이름이 Hermione, Harry, Hagrid 와 같이 적다면
연결 리스트로 처리하는 것이 효율적이다.





8) 트라이 (retrieval)

트라이는 기본적으로 트리 형태의 자료 구조이지만
각 노드가 배열로 이루어져있다는 점에서 다르다.

만약 트라이로 DASOL을 저장한다면,
맨 처음 알파벳을 저장하는 노드는 a부터 z까지의 값을 가지는 배열이 되고
다음 층의 a - z 배열을 가리킨다.
그렇게 5층의 배열이 각각의 D, A, S, O, L을 저장하며
다음 배열을 가리키는 포인터를 가진다.

트라이에서 값을 검색하는 데에는
문자열의 길이, 즉 이름의 길이만큼의 시간이 필요하다.
DASOL을 검색하기 위해 5층의 배열을 탐색한 것처럼
트라이는 O(n)의 상한 시간을 가진다.





9) 스택, 큐, 딕셔너리


큐(queues) 
: FIFO 선입선출의 구조를 가지는 자료 구조.
  가장 먼저 들어온 값이 가장 먼저 나간다.
  가게에서 줄을 서는 것과 비슷하다.
  큐 안에 들어가는 것을 enqueue, 나오는 것을 dequeue라고 한다.
  
스택(stack)
 : LIFO 선입후출의 구조를 가지는 자료 구조. 
   가장 나중에 들어온 값이 가장 먼저 나간다.
   뷔페에서 접시를 쌓아 뒀을 때 사람들이 맨 위의 접시를 가장 먼저 집는 것과 같다.
   스택 안에 들어가는 것을 push, 나오는 것을 pop이라고 부른다.
   

딕셔너리(dictionary)
 : 키와 값이라는 요소로 이루어져 있다.
   ex) 20156084 : Hermione, 20157865 : Harry





"""