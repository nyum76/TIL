# table

||열|||
|-|-|-|-|
||열|||
|행|셀|행|행|
||열|||
- 행 ( row ) 
- 열 ( column )
- 셀 ( cell )

## table 태그
```html
<table></table>
```

## caption 태그
**표 제목**
```html
<table>
  <caption>표 제목</caption>
</table>
```

## tr 태그
**(table row) 행 생성**
```html
<table>
  <tr></tr>
</table>
```

## th, td 태그

- **th** (table header) : **제목 열** 생성
- **td** (table data) : **일반** 데이터 **열** 생성
```html
<table>
  <th>제목</th>
  </td>내용</td>
</table>
```

## rowspan colspan 속성

- **rowspan** : 행과 행 병합
- **colspan** : 열과 열 병합

```html
<td rowspan="3">hi</td>

<td colspan="2">hello</td>
```
속성값으로 병합하고 싶은 셀의 개수 입력

**병합한 셀의 개수만큼** 다음 행 또는 열을 **비워둬야함**


## thead, tfoot, tbody 태그
**반드시 아래 순서로 사용**
- **thead** 태그 : 헤더 영역 행, 한 번만 사용, th 태그로 열 생성
- **tfoot** 태그 : 푸터 영역 행, 한 번만 사용
- **tbody** 태그 : 본문 영역 행

## col, colgroup 태그

열 전체를 그룹화 해 통일된 스타일 적용함

- **col** 태그: 하나의 열 그룹화
- **colgroup** 태그 : 여러개 열 그룹화
  - span : 그룹화 할 열 개수

## scope 속성

제목을 나타내는 셀의 범위 지정

- th 태그에서만 사용
- col, colgroup, row 를 값으로 사용
  - col (열) : 세로 방향
  - row (행) : 가로 방향