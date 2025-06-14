# [Platinum IV] K번째 최단경로 찾기 - 1854 

[문제 링크](https://www.acmicpc.net/problem/1854) 

### 성능 요약

메모리: 57696 KB, 시간: 708 ms

### 분류

그래프 이론, 자료 구조, 집합과 맵, 최단 경로, 데이크스트라, 우선순위 큐

### 제출 일자

2025년 2월 12일 10:58:27

### 문제 설명

<p>봄캠프를 마친 김진영 조교는 여러 도시를 돌며 여행을 다닐 계획이다. 그런데 김 조교는, '느림의 미학'을 중요시하는 사람이라 항상 최단경로로만 이동하는 것은 별로 좋아하지 않는다. 하지만 너무 시간이 오래 걸리는 경로도 그리 매력적인 것만은 아니어서, 적당한 타협안인 '$k$번째 최단경로'를 구하길 원한다. 그를 돕기 위한 프로그램을 작성해 보자.</p>

### 입력 

 <p>첫째 줄에 $n$, $m$, $k$가 주어진다. ($1 ≤ n ≤ 1\,000$, $0 ≤ m ≤ 250\,000$, $1 ≤ k ≤ 100$, $mk ≤ 3\,000\,000$) $n$과 $m$은 각각 김 조교가 여행을 고려하고 있는 도시들의 개수와, 도시 간에 존재하는 도로의 수이다.</p>

<p>이어지는 $m$개의 줄에는 각각 도로의 정보를 제공하는 세 개의 정수 $a$, $b$, $c$가 포함되어 있다. 이것은 $a$번 도시에서 $b$번 도시로 갈 때는 $c$의 시간이 걸린다는 의미이다. ($1 ≤ a, b ≤ n$, $1 ≤ c ≤ 1\,000$)</p>

<p>도시의 번호는 $1$번부터 $n$번까지 연속하여 붙어 있으며, $1$번 도시는 시작도시이다. 두 도로의 시작점과 도착점이 모두 같은 경우는 없다.</p>

### 출력 

 <p>$n$개의 줄을 출력한다. $i$번째 줄에 $1$번 도시에서 $i$번 도시로 가는 $k$번째 최단경로의 소요시간을 출력한다.</p>

<p>경로의 소요시간은 경로 위에 있는 도로들을 따라 이동하는데 필요한 시간들의 합이다. $i$번 도시에서 $i$번 도시로 가는 최단경로는 $0$이지만, 일반적인 $k$번째 최단경로는 $0$이 아닐 수 있음에 유의한다. 또, $k$번째 최단경로가 존재하지 않으면 $-1$을 출력한다. 최단경로에 같은 정점이 여러 번 포함되어도 된다.</p>

