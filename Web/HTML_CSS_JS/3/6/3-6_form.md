# form 
HTML 에서 상호작용해 정보를 입력받고 서버로 전송하기 위한 양식

## form 태그

```html
<form action="서버 url" method="get or post"></form>
```
- `action` : 폼 요소에서 입력받은 값을 전송할 서버의 URL
- `method` : 서버에 전송할 때의 **송신 방식** ( get 또는 post )

## input 태그

```html
<input type="종류" name="이름" value="초깃값">
```
- `type` : ( 필수 ) 상호작용 요소의 종류 결정
  - 예시 : [input type 속성](input.html) 
- `name` : 입력 요소의 이름, 입력 요소가 서버로 전송될 때, name 에 적힌 값이 이름으로 지정됨
- `value` : 입력 요소의 초깃값

## lable 태그
상호작용 요소에 이름 붙임


label 로 설정한 이름을 클릭해 상호작용 요소를 선택할 수 있음

```html
<label for="userid">ID</label>
<input type="text" id="userid">
```
- label의 **for** 과 input 의 **id** **속성값을 일치**시켜줘야 함

## fieldset & legend

```html
<form>
  <fieldset>
    <legend>TEAM</legend>
  </fieldset>
</form>
```
- `fieldset` : 상호작용 요소를 그룹짓는 태그
- `legend` : fieldset의 그룹에 이름을 붙이는 태그

## textarea 태그

```html
<textarea>초깃값</textarea>


<form action="#" method="post">
  <fieldset>
    <legend>post</legend>
    <p>
      <label for="desc">
        <textarea id="desc" name="desc"></textarea>
      </label>
    </p>
  </fieldset>
</form>
```

## select, option, optgroup 태그

```html
<select>
  <optgroup label="korea team">
    <option value="DRX">DRX</option>
    <option value="Gen.G">Gen.G</option>
    <option value="NS">NS</option>
    <option value="T1">T1</option>
  </optgroup>
  <optgroup label="japan team">
    <option value="ZETA">ZETA</option>
    <option value="DFM">DFM</option>
  </optgroup>
</select>
```
- `select` 태그 : 콤보박스 생성
  - size : 콤보박스 화면에 노출되는 항목 갯수
  - multiple : CTRL/CMD 를 누르고 여러 항목 선택
- `option` 태그 : 콤보박스 항목
  - selected : 기본 선택 항목
- `optgroup` 태그 : 항목들을 그룹으로 묶음

## button 태그

```html
<button type="종류">버튼 내용</button>
```
- type
  - submit : 서버에 폼 전송
  - reset : 상호작용 요소에 입력된 내용 초기화 버튼
  - button : 단순한 버튼

---

## 그 외 다양한 상호작용 속성

### disabled
상호작용 요소 비활성화

### readonly
상호작용 요소 읽기 전용 (수정 or 입력 X, 복사 O)

### maxlength
입력할 수 있는 글자 수 제한

`input type=`
- `text`
- `search`
- `url`
- `tel`
- `email`
- `password`
- `date`
- `month`
- `week`
- `time`
- `datetime-local`
- `number`
### checked

요소를 선택된 상태로 표시

`input type=`
- `checkbox`
- `radio`

### placeholder

입력값에 대한 힌트