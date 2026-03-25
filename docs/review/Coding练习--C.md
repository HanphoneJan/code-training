# 数据结构
### 链表
```c
#include <stdio.h>
#include <stdlib.h>

// 单向链表节点定义
typedef struct SNode {
    int data;
    struct SNode* next;
} SNode;

// 双向链表节点定义
typedef struct DNode {
    int data;
    struct DNode* prev;
    struct DNode* next;
} DNode;

// 单向链表插入
void sInsert(SNode** head, int data) {
    SNode* newNode = (SNode*)malloc(sizeof(SNode));
    newNode->data = data;
    newNode->next = *head;
    *head = newNode;
}

// 单向链表查找
SNode* sSearch(SNode* head, int data) {
    SNode* current = head;
    while (current != NULL) {
        if (current->data == data) return current;
        current = current->next;
    }
    return NULL;
}

// 双向链表插入
void dInsert(DNode** head, int data) {
    DNode* newNode = (DNode*)malloc(sizeof(DNode));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = *head;
    if (*head != NULL) (*head)->prev = newNode;
    *head = newNode;
}

// 双向链表查找
DNode* dSearch(DNode* head, int data) {
    DNode* current = head;
    while (current != NULL) {
        if (current->data == data) return current;
        current = current->next;
    }
    return NULL;
}

// 循环链表插入
void cInsert(SNode** head, int data) {
    SNode* newNode = (SNode*)malloc(sizeof(SNode));
    newNode->data = data;
    if (*head == NULL) {
        newNode->next = newNode;
        *head = newNode;
    } else {
        newNode->next = (*head)->next;
        (*head)->next = newNode;
        int temp = (*head)->data;
        (*head)->data = newNode->data;
        newNode->data = temp;
    }
}

// 循环链表查找
SNode* cSearch(SNode* head, int data) {
    if (head == NULL) return NULL;
    SNode* current = head;
    do {
        if (current->data == data) return current;
        current = current->next;
    } while (current != head);
    return NULL;
}

}    
```

### 栈（Stack）
​

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

// 定义栈结构
typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

// 初始化栈
void initStack(Stack *s) {
    s->top = -1;
}

// 判断栈是否为空
int isEmpty(Stack *s) {
    return s->top == -1;
}

// 判断栈是否已满
int isFull(Stack *s) {
    return s->top == MAX_SIZE - 1;
}

// 入栈操作
void push(Stack *s, int value) {
    if (!isFull(s)) {
        s->data[++(s->top)] = value;
    }
}

// 出栈操作
int pop(Stack *s) {
    if (!isEmpty(s)) {
        return s->data[(s->top)--];
    }
    return -1;
}

// 获取栈顶元素
int peek(Stack *s) {
    if (!isEmpty(s)) {
        return s->data[s->top];
    }
    return -1;
}

// 括号匹配
int isBalanced(char *expression) {
    Stack s;
    initStack(&s);
    for (int i = 0; expression[i] != '\0'; i++) {
        if (expression[i] == '(') {
            push(&s, 1);
        } else if (expression[i] == ')') {
            if (isEmpty(&s)) {
                return 0;
            }
            pop(&s);
        }
    }
    return isEmpty(&s);
}

// 简单的后缀表达式求值
int evaluatePostfix(char *expression) {
    Stack s;
    initStack(&s);
    for (int i = 0; expression[i] != '\0'; i++) {
        if (expression[i] >= '0' && expression[i] <= '9') {
            push(&s, expression[i] - '0');
        } else {
            int operand2 = pop(&s);
            int operand1 = pop(&s);
            switch (expression[i]) {
                case '+':
                    push(&s, operand1 + operand2);
                    break;
                case '-':
                    push(&s, operand1 - operand2);
                    break;
                case '*':
                    push(&s, operand1 * operand2);
                    break;
                case '/':
                    push(&s, operand1 / operand2);
                    break;
            }
        }
    }
    return pop(&s);
}
```

### 队列（Queue）

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

// 顺序队列
typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
} SeqQueue;

// 初始化顺序队列
void initSeqQueue(SeqQueue *q) {
    q->front = q->rear = 0;
}

// 顺序队列入队
int seqEnqueue(SeqQueue *q, int value) {
    if (q->rear == MAX_SIZE) {
        return 0; // 队列已满
    }
    q->data[q->rear++] = value;
    return 1;
}

// 顺序队列出队
int seqDequeue(SeqQueue *q) {
    if (q->front == q->rear) {
        return -1; // 队列为空
    }
    return q->data[q->front++];
}

// 循环队列
typedef struct {
    int data[MAX_SIZE];
    int front;
    int rear;
} CirQueue;

// 初始化循环队列
void initCirQueue(CirQueue *q) {
    q->front = q->rear = 0;
}

// 循环队列入队
int cirEnqueue(CirQueue *q, int value) {
    if ((q->rear + 1) % MAX_SIZE == q->front) {
        return 0; // 队列已满
    }
    q->data[q->rear] = value;
    q->rear = (q->rear + 1) % MAX_SIZE;
    return 1;
}

// 循环队列出队
int cirDequeue(CirQueue *q) {
    if (q->front == q->rear) {
        return -1; // 队列为空
    }
    int value = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    return value;
}

// 简单的广度优先搜索模拟（使用循环队列）
void bfsSimulation() {
    CirQueue q;
    initCirQueue(&q);
    cirEnqueue(&q, 1);
    while (q.front != q.rear) {
        int node = cirDequeue(&q);
        printf("访问节点: %d\n", node);
        // 模拟扩展节点
        if (node * 2 <= 10) {
            cirEnqueue(&q, node * 2);
        }
        if (node * 2 + 1 <= 10) {
            cirEnqueue(&q, node * 2 + 1);
        }
    }
}

int main() {
    // 顺序队列测试
    SeqQueue seqQ;
    initSeqQueue(&seqQ);
    seqEnqueue(&seqQ, 1);
    seqEnqueue(&seqQ, 2);
    printf("顺序队列出队元素: %d\n", seqDequeue(&seqQ));

    // 循环队列测试
    CirQueue cirQ;
    initCirQueue(&cirQ);
    cirEnqueue(&cirQ, 3);
    cirEnqueue(&cirQ, 4);
    printf("循环队列出队元素: %d\n", cirDequeue(&cirQ));

    // 广度优先搜索模拟
    bfsSimulation();

    return 0;
}    
```


- 应用：文件系统目录结构、数据库索引、编译原理语法树。

```c
#include <stdio.h>
#include <stdlib.h>

// 定义二叉树节点结构
typedef struct TreeNode {
    int data;
    int height;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

// 获取节点高度
int height(TreeNode *node) {
    return node ? node->height : 0;
}

// 获取两个数中的最大值
int max(int a, int b) {
    return a > b ? a : b;
}

// 创建新节点
TreeNode* newNode(int data) {
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    node->data = data;
    node->left = node->right = NULL;
    node->height = 1;
    return node;
}

// 右旋操作
TreeNode* rightRotate(TreeNode *y) {
    TreeNode *x = y->left;
    TreeNode *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right)) + 1;
    x->height = max(height(x->left), height(x->right)) + 1;

    return x;
}

// 左旋操作
TreeNode* leftRotate(TreeNode *x) {
    TreeNode *y = x->right;
    TreeNode *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

// 获取平衡因子
int getBalance(TreeNode *node) {
    return node ? height(node->left) - height(node->right) : 0;
}

// 插入节点到 AVL 树
TreeNode* insertAVL(TreeNode* node, int data) {
    if (!node) return newNode(data);

    if (data < node->data)
        node->left = insertAVL(node->left, data);
    else if (data > node->data)
        node->right = insertAVL(node->right, data);
    else
        return node;

    node->height = 1 + max(height(node->left), height(node->right));

    int balance = getBalance(node);

    // 左左情况
    if (balance > 1 && data < node->left->data)
        return rightRotate(node);

    // 右右情况
    if (balance < -1 && data > node->right->data)
        return leftRotate(node);

    // 左右情况
    if (balance > 1 && data > node->left->data) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // 右左情况
    if (balance < -1 && data < node->right->data) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

// 插入节点到二叉搜索树
TreeNode* insertBST(TreeNode* root, int data) {
    if (root == NULL) {
        return newNode(data);
    }
    if (data < root->data) {
        root->left = insertBST(root->left, data);
    } else if (data > root->data) {
        root->right = insertBST(root->right, data);
    }
    return root;
}

// 查找二叉搜索树中的最小节点
TreeNode* minValueNode(TreeNode* node) {
    TreeNode* current = node;
    while (current && current->left != NULL)
        current = current->left;
    return current;
}

// 从二叉搜索树中删除节点
TreeNode* deleteNode(TreeNode* root, int data) {
    if (root == NULL) return root;

    if (data < root->data)
        root->left = deleteNode(root->left, data);
    else if (data > root->data)
        root->right = deleteNode(root->right, data);
    else {
        if (root->left == NULL) {
            TreeNode *temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            TreeNode *temp = root->left;
            free(root);
            return temp;
        }
        TreeNode* temp = minValueNode(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

// 前序遍历
void preOrder(TreeNode *root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preOrder(root->left);
        preOrder(root->right);
    }
}

// 中序遍历
void inOrder(TreeNode *root) {
    if (root != NULL) {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

// 后序遍历
void postOrder(TreeNode *root) {
    if (root != NULL) {
        postOrder(root->left);
        postOrder(root->right);
        printf("%d ", root->data);
    }
}
```



### 图（Graph）


```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_VERTICES 100

// 邻接表节点
typedef struct Node {
    int vertex;
    int weight;
    struct Node* next;
} Node;

// 邻接表图结构
typedef struct {
    Node* adjList[MAX_VERTICES];
    int numVertices;
} GraphList;

// 邻接矩阵图结构
typedef struct {
    int adjMatrix[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
} GraphMatrix;

// 创建邻接表图
GraphList* createGraphList(int vertices) {
    GraphList* graph = (GraphList*)malloc(sizeof(GraphList));
    graph->numVertices = vertices;
    for (int i = 0; i < vertices; i++) {
        graph->adjList[i] = NULL;
    }
    return graph;
}

// 创建邻接矩阵图
GraphMatrix* createGraphMatrix(int vertices) {
    GraphMatrix* graph = (GraphMatrix*)malloc(sizeof(GraphMatrix));
    graph->numVertices = vertices;
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            graph->adjMatrix[i][j] = 0;
        }
    }
    return graph;
}

// 邻接表插入边
void insertEdgeList(GraphList* graph, int src, int dest, int weight) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = dest;
    newNode->weight = weight;
    newNode->next = graph->adjList[src];
    graph->adjList[src] = newNode;
}

// 邻接矩阵插入边
void insertEdgeMatrix(GraphMatrix* graph, int src, int dest, int weight) {
    graph->adjMatrix[src][dest] = weight;
}

// 邻接表删除边
void deleteEdgeList(GraphList* graph, int src, int dest) {
    Node* current = graph->adjList[src];
    Node* prev = NULL;
    while (current != NULL && current->vertex != dest) {
        prev = current;
        current = current->next;
    }
    if (current != NULL) {
        if (prev == NULL) {
            graph->adjList[src] = current->next;
        } else {
            prev->next = current->next;
        }
        free(current);
    }
}

// 邻接矩阵删除边
void deleteEdgeMatrix(GraphMatrix* graph, int src, int dest) {
    graph->adjMatrix[src][dest] = 0;
}

// 深度优先搜索辅助函数（邻接表）
void DFSListUtil(GraphList* graph, int vertex, bool visited[]) {
    visited[vertex] = true;
    printf("%d ", vertex);
    Node* current = graph->adjList[vertex];
    while (current != NULL) {
        int adjVertex = current->vertex;
        if (!visited[adjVertex]) {
            DFSListUtil(graph, adjVertex, visited);
        }
        current = current->next;
    }
}

// 深度优先搜索（邻接表）
void DFSList(GraphList* graph, int start) {
    bool visited[MAX_VERTICES] = {false};
    DFSListUtil(graph, start, visited);
    printf("\n");
}

// 深度优先搜索辅助函数（邻接矩阵）
void DFSMatrixUtil(GraphMatrix* graph, int vertex, bool visited[]) {
    visited[vertex] = true;
    printf("%d ", vertex);
    for (int i = 0; i < graph->numVertices; i++) {
        if (graph->adjMatrix[vertex][i] != 0 && !visited[i]) {
            DFSMatrixUtil(graph, i, visited);
        }
    }
}

// 深度优先搜索（邻接矩阵）
void DFSMatrix(GraphMatrix* graph, int start) {
    bool visited[MAX_VERTICES] = {false};
    DFSMatrixUtil(graph, start, visited);
    printf("\n");
}

// 广度优先搜索（邻接表）
void BFSList(GraphList* graph, int start) {
    bool visited[MAX_VERTICES] = {false};
    int queue[MAX_VERTICES];
    int front = 0, rear = 0;

    visited[start] = true;
    queue[rear++] = start;

    while (front < rear) {
        int vertex = queue[front++];
        printf("%d ", vertex);
        Node* current = graph->adjList[vertex];
        while (current != NULL) {
            int adjVertex = current->vertex;
            if (!visited[adjVertex]) {
                visited[adjVertex] = true;
                queue[rear++] = adjVertex;
            }
            current = current->next;
        }
    }
    printf("\n");
}

// 广度优先搜索（邻接矩阵）
void BFSMatrix(GraphMatrix* graph, int start) {
    bool visited[MAX_VERTICES] = {false};
    int queue[MAX_VERTICES];
    int front = 0, rear = 0;

    visited[start] = true;
    queue[rear++] = start;

    while (front < rear) {
        int vertex = queue[front++];
        printf("%d ", vertex);
        for (int i = 0; i < graph->numVertices; i++) {
            if (graph->adjMatrix[vertex][i] != 0 && !visited[i]) {
                visited[i] = true;
                queue[rear++] = i;
            }
        }
    }
    printf("\n");
}

// Dijkstra 算法（邻接矩阵）
void dijkstra(GraphMatrix* graph, int start) {
    int dist[MAX_VERTICES];
    bool sptSet[MAX_VERTICES];

    for (int i = 0; i < graph->numVertices; i++) {
        dist[i] = INT_MAX;
        sptSet[i] = false;
    }

    dist[start] = 0;

    for (int count = 0; count < graph->numVertices - 1; count++) {
        int minDist = INT_MAX, minIndex;
        for (int v = 0; v < graph->numVertices; v++) {
            if (!sptSet[v] && dist[v] <= minDist) {
                minDist = dist[v];
                minIndex = v;
            }
        }
        sptSet[minIndex] = true;
        for (int v = 0; v < graph->numVertices; v++) {
            if (!sptSet[v] && graph->adjMatrix[minIndex][v] && dist[minIndex] != INT_MAX && dist[minIndex] + graph->adjMatrix[minIndex][v] < dist[v]) {
                dist[v] = dist[minIndex] + graph->adjMatrix[minIndex][v];
            }
        }
    }

    printf("顶点到 %d 的最短距离:\n", start);
    for (int i = 0; i < graph->numVertices; i++) {
        printf("%d: %d\n", i, dist[i]);
    }
}
```

# 算法
### 排序算法

```c
#include <stdio.h>
#include <stdlib.h>

// 冒泡排序
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// 插入排序
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// 选择排序
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        int temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}

// 归并排序辅助函数：合并两个子数组
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// 归并排序
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

// 快速排序辅助函数：分区
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}

// 快速排序
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// 堆排序辅助函数：调整堆
void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest])
        largest = l;
    if (r < n && arr[r] > arr[largest])
        largest = r;
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

// 堆排序
void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}

// 基数排序辅助函数：获取最大数
int getMax(int arr[], int n) {
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}

// 基数排序辅助函数：计数排序
void countSort(int arr[], int n, int exp) {
    int output[n];
    int count[10] = {0};
    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

// 基数排序
void radixSort(int arr[], int n) {
    int m = getMax(arr, n);
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp);
}

// 打印数组
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    return 0;
}
    
```


### 查找算法

```c
#include <stdio.h>
#include <stdlib.h>

// 线性查找
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

// 二分查找
int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

#define TABLE_SIZE 10

// 哈希表节点
typedef struct HashNode {
    int key;
    int value;
    struct HashNode* next;
} HashNode;

// 哈希表
typedef struct {
    HashNode* table[TABLE_SIZE];
} HashTable;

// 初始化哈希表
void initHashTable(HashTable* ht) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        ht->table[i] = NULL;
    }
}

// 哈希函数
int hashFunction(int key) {
    return key % TABLE_SIZE;
}

// 插入哈希表
void insertHash(HashTable* ht, int key, int value) {
    int index = hashFunction(key);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->value = value;
    newNode->next = ht->table[index];
    ht->table[index] = newNode;
}

// 哈希查找
int hashSearch(HashTable* ht, int key) {
    int index = hashFunction(key);
    HashNode* current = ht->table[index];
    while (current != NULL) {
        if (current->key == key) {
            return current->value;
        }
        current = current->next;
    }
    return -1;
}

// 二叉搜索树节点
typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// 插入二叉搜索树
TreeNode* insertBST(TreeNode* root, int data) {
    if (root == NULL) {
        TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
        newNode->data = data;
        newNode->left = newNode->right = NULL;
        return newNode;
    }
    if (data < root->data) {
        root->left = insertBST(root->left, data);
    } else if (data > root->data) {
        root->right = insertBST(root->right, data);
    }
    return root;
}

// 二叉搜索树查找
TreeNode* searchBST(TreeNode* root, int target) {
    if (root == NULL || root->data == target) {
        return root;
    }
    if (target < root->data) {
        return searchBST(root->left, target);
    }
    return searchBST(root->right, target);
}

int main() {
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 50;

    // 线性查找
    int linearResult = linearSearch(arr, n, target);
    if (linearResult != -1) {
        printf("线性查找: 找到 %d 在索引 %d\n", target, linearResult);
    } else {
        printf("线性查找: 未找到 %d\n", target);
    }

    // 二分查找
    int binaryResult = binarySearch(arr, 0, n - 1, target);
    if (binaryResult != -1) {
        printf("二分查找: 找到 %d 在索引 %d\n", target, binaryResult);
    } else {
        printf("二分查找: 未找到 %d\n", target);
    }

    // 哈希查找
    HashTable ht;
    initHashTable(&ht);
    for (int i = 0; i < n; i++) {
        insertHash(&ht, arr[i], i);
    }
    int hashResult = hashSearch(&ht, target);
    if (hashResult != -1) {
        printf("哈希查找: 找到 %d 在索引 %d\n", target, hashResult);
    } else {
        printf("哈希查找: 未找到 %d\n", target);
    }

    // 二叉搜索树查找
    TreeNode* root = NULL;
    for (int i = 0; i < n; i++) {
        root = insertBST(root, arr[i]);
    }
    TreeNode* bstResult = searchBST(root, target);
    if (bstResult != NULL) {
        printf("二叉搜索树查找: 找到 %d\n", target);
    } else {
        printf("二叉搜索树查找: 未找到 %d\n", target);
    }

    return 0;
}
    
```

### 字符串算法

```c
#include <stdio.h>
#include <string.h>

// 计算前缀函数
void computeLPSArray(char* pat, int M, int* lps) {
    int len = 0;
    lps[0] = 0;
    int i = 1;
    while (i < M) {
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

// KMP 算法
int KMPSearch(char* pat, char* txt) {
    int M = strlen(pat);
    int N = strlen(txt);
    int lps[M];
    computeLPSArray(pat, M, lps);
    int i = 0;
    int j = 0;
    while (i < N) {
        if (pat[j] == txt[i]) {
            j++;
            i++;
        }
        if (j == M) {
            return i - j;
        } else if (i < N && pat[j] != txt[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return -1;
}

// BF 算法
int BFSearch(char* pat, char* txt) {
    int M = strlen(pat);
    int N = strlen(txt);
    for (int i = 0; i <= N - M; i++) {
        int j;
        for (j = 0; j < M; j++) {
            if (txt[i + j] != pat[j]) {
                break;
            }
        }
        if (j == M) {
            return i;
        }
    }
    return -1;
}

int main() {
    char txt[] = "ABABDABACDABABCABAB";
    char pat[] = "ABABCABAB";

    // KMP 算法
    int kmpResult = KMPSearch(pat, txt);
    if (kmpResult != -1) {
        printf("KMP 算法找到匹配，起始位置为: %d\n", kmpResult);
    } else {
        printf("KMP 算法未找到匹配\n");
    }

    // BF 算法
    int bfResult = BFSearch(pat, txt);
    if (bfResult != -1) {
        printf("BF 算法找到匹配，起始位置为: %d\n", bfResult);
    } else {
        printf("BF 算法未找到匹配\n");
    }

    return 0;
}    
```

