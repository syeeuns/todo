# ToDo List
Javascript 이용한 간단한 ToDoList <br>

![todo](https://user-images.githubusercontent.com/72585287/116176696-8a53cc00-a74d-11eb-86a1-19fdb1edd0e0.png)

<br>

## 설명
### 0. 연결하기
html 파일 body 맨 마지막에 
`<script src="todo.js"></script>` 추가하여 JS파일 연결
JS파일에서 `document.querySelector("선택자")` 로 태그 선택

### 1. todo 불러오기
개발자도구 -> Application -> Local storage
key가 toDos 인 항목이 있으면 값을 불러오기

- `localstorage` : 브라우저의 저장소, 브라우저가 닫혀도 유지
- `localstorage.getItem(key)` : key에 해당하는 값 가져오기
- `JSON.parse(내용)` : JSON 형식의 문자열을 자바스크립트 객체로 변환

JS 객체로 변환하고, text로 변환하여 보여주기

### 2. todo list만들어서 보여주기
- `document.createElement("생성할 요소")` : html에 요소 생성
- `innerText` : 요소 안에 들어갈 text  설정
- `addEventListener(이벤트, 함수)` : 지정한 이벤트가 발생할 때마다 호출할 함수 지정
- `부모.appendChild(자식)` : 한 노드를 특정 부모 노드의 자식 노드 리스트 중 마지막 자식으로 추가

li, button, span 생성
li 의 자식으로 span, button 추가
li 의 id는 todo list에 추가된 순서대로 1,2,3...
html의 ul 의 자식으로 li  추가
todo 객체 생성해서 배열에 추가 후 저장

### 3. 기록한 todo list 저장하기
`localstorage.setItem(설정할 key, JSON 형식 문자열);`

### 4. delete 버튼으로 todo list 삭제하기
button 눌리면 그 버튼의 parentNode인 li를  todo list 에서 삭제

- `filter()` : 인자로 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환

### 5. Input에 제출됐을 때, 이벤트 관리
- `event.preventDefault()` : "submit" 이벤트 발생할 때마다  reload되는데, 그거 막음 
- 현재 input 창에 있는 값을 todoList 추가 (보여주기, 저장)


### 6. list 목록 아이템 앞에 아이콘 추가
```css
ul li:before{
    content: "💎";
    display: inline-block;
    vertical-align: middle;
    padding: 0px 5px 5px 0px;
  }
```
