# HTML 태그
## div
- **div**ision
- **블록** 요소
- 특별한 의미는 없지만 **구분을 위해 사용**!
## h1 ~ h6
- **h**eading : **제목**
- **블록** 요소
- h 뒤의 숫자가 작을수록 더 중요한 제목

‼️ 글자를 다루기에 인라인 요소라고 착각하기 쉽지만, 제목을 나타내는 블록 요소이다!
## p
- **p**aragraph : **문장**
- **블록** 요소

## img
- **im**a**g**e : **이미지 삽입**
- **인라인** 요소
- 이미지가 출력되지 못할 경우에 나타날 텍스트를 `alt`(alternative) 속성에 입력

## ul li
- **u**nordered **l**ist : 순서가 필요 없는 목록
- **list** **i**tem : 목록의 각 항목
- **ul** 과 **li** 는 **한 세트**임

## ol li
- **o**rdered **l**ist : 순서형 목록

## a
- **a**nchor (닻) : **하이퍼링크**
  - 닻을 내린다 = 링크를 건다
- **인라인** 요소
- `target` 속성 : 어떤 브라우저 탭에서 열릴지 지정
  - `target=_blank` 새 탭에서 페이지 열기
## span
- 특별한 의미 없이 **텍스트 구분**을 위해 사용
- **인라인** 요소
## br
- **br**eak : 줄바꿈
‼️ HTML 코드에서 `Enter` 로 줄바꿈해도 적용이 안 됨

## input
- 인라인-블록 요소
  - 기본 특징은 모두 인라인 요소와 같음
  - 가로/세로 너비, 위/아래/좌/우 여백 모두 지정 (블록 요소 특징)
- `type` 속성 : 사용자에게 입력받을 **데이터 타입 지정**
  - `checkbox` : 다중 선택, `checked` 를 사용해 기본값을 선택됨으로 지정 가능
  - `radio` : 택 1
- `value` 속성 : 원하는 **입력 요소 미리 지정**
- `placeholder` 속성 : 입력 요소 값이 없을 때, 사용자에게 **힌트**를 줌
- `disabled` 속성 : 입력 요소 비활성화

## table
- **표** 생성
- 행(Row) 열(Column)
- **t**able **r**ow : 행
- **t**able **d**ata : 열







## div p 태그 사용해보기
```html
<!-- div 태그 -->
<div class="DRX">
  <p>Mako</p>
  <p>Beyn</p>
  <p>Freeing</p>
  <p>Hyunmin</p>
  <p>Astrella</p>
</div>
<div class="Gen.G">
  <p>T3xture</p>
  <p>Karon</p>
  <p>Munchikin</p>
  <p>Ash</p>
  <p>Foxy9</p>
</div>
```
블록 요소와 인라인 요소를 그룹으로 묶음
관련 있는 요소를 그룹으로 묶어 HTML 구조를 깔끔하게 유지


```html
<!-- span 태그 -->
<p>제가 가장 좋아하는 선수는 <span>T3xture</span>선수입니다</p>
```
인라인 요소를 그룹으로 묶음
