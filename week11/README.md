# 신규 아이디 추천
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>카카오에 입사한 신입 개발자 <code>네오</code>는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다. "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.<br>
다음은 카카오 아이디의 규칙입니다.</p>

<ul>
<li>아이디의 길이는 3자 이상 15자 이하여야 합니다.</li>
<li>아이디는 알파벳 소문자, 숫자, 빼기(<code>-</code>), 밑줄(<code>_</code>), 마침표(<code>.</code>) 문자만 사용할 수 있습니다.</li>
<li>단, 마침표(<code>.</code>)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.</li>
</ul>

<p>"네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.<br>
신규 유저가 입력한 아이디가 <code>new_id</code> 라고 한다면,</p>
<div class="highlight"><pre class="codehilite"><code>1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
</code></pre></div>
<hr>

<p>예를 들어, new_id 값이 "...!@BaT#*..y.abcdefghijklm" 라면, 위 7단계를 거치고 나면 new_id는 아래와 같이 변경됩니다.</p>

<p>1단계 대문자 'B'와 'T'가 소문자 'b'와 't'로 바뀌었습니다.<br>
<code>"...!@BaT#*..y.abcdefghijklm"</code> → <code>"...!@bat#*..y.abcdefghijklm"</code></p>

<p>2단계 '!', '@', '#', '*' 문자가 제거되었습니다.<br>
<code>"...!@bat#*..y.abcdefghijklm"</code> → <code>"...bat..y.abcdefghijklm"</code></p>

<p>3단계 '...'와 '..' 가 '.'로 바뀌었습니다.<br>
<code>"...bat..y.abcdefghijklm"</code> → <code>".bat.y.abcdefghijklm"</code></p>

<p>4단계 아이디의 처음에 위치한 '.'가 제거되었습니다.<br>
<code>".bat.y.abcdefghijklm"</code> → <code>"bat.y.abcdefghijklm"</code></p>

<p>5단계 아이디가 빈 문자열이 아니므로 변화가 없습니다.<br>
<code>"bat.y.abcdefghijklm"</code> → <code>"bat.y.abcdefghijklm"</code></p>

<p>6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거되었습니다.<br>
<code>"bat.y.abcdefghijklm"</code> → <code>"bat.y.abcdefghi"</code></p>

<p>7단계 아이디의 길이가 2자 이하가 아니므로 변화가 없습니다.<br>
<code>"bat.y.abcdefghi"</code> → <code>"bat.y.abcdefghi"</code></p>

<p>따라서 신규 유저가 입력한 new_id가 "...!@BaT#*..y.abcdefghijklm"일 때, 네오의 프로그램이 추천하는 새로운 아이디는 "bat.y.abcdefghi" 입니다.</p>

<hr>

<h4><strong>[문제]</strong></h4>

<p>신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.</p>

<h4><strong>[제한사항]</strong></h4>

<p>new_id는 길이 1 이상 1,000 이하인 문자열입니다.<br>
new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.<br>
new_id에 나타날 수 있는 특수문자는 <code>-_.~!@#$%^&amp;*()=+[{]}:?,&lt;&gt;/</code> 로 한정됩니다.</p>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>no</th>
<th>new_id</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>예1</td>
<td><code>"...!@BaT#*..y.abcdefghijklm"</code></td>
<td><code>"bat.y.abcdefghi"</code></td>
</tr>
<tr>
<td>예2</td>
<td><code>"z-+.^."</code></td>
<td><code>"z--"</code></td>
</tr>
<tr>
<td>예3</td>
<td><code>"=.="</code></td>
<td><code>"aaa"</code></td>
</tr>
<tr>
<td>예4</td>
<td><code>"123_.def"</code></td>
<td><code>"123_.def"</code></td>
</tr>
<tr>
<td>예5</td>
<td><code>"abcdefghijklmn.p"</code></td>
<td><code>"abcdefghijklmn"</code></td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<hr>

<p><strong>입출력 예 #1</strong><br>
문제의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong><br>
7단계를 거치는 동안 new_id가 변화하는 과정은 아래와 같습니다.</p>

<p>1단계 변화 없습니다.<br>
2단계 <code>"z-+.^."</code> → <code>"z-.."</code><br>
3단계 <code>"z-.."</code> → <code>"z-."</code><br>
4단계 <code>"z-."</code> → <code>"z-"</code><br>
5단계 변화 없습니다.<br>
6단계 변화 없습니다.<br>
7단계 <code>"z-"</code> → <code>"z--"</code></p>

<p><strong>입출력 예 #3</strong><br>
7단계를 거치는 동안 new_id가 변화하는 과정은 아래와 같습니다.</p>

<p>1단계 변화 없습니다.<br>
2단계 <code>"=.="</code> → <code>"."</code><br>
3단계 변화 없습니다.<br>
4단계 <code>"."</code> → <code>""</code> (new_id가 빈 문자열이 되었습니다.)<br>
5단계 <code>""</code> → <code>"a"</code><br>
6단계 변화 없습니다.<br>
7단계 <code>"a"</code> → <code>"aaa"</code></p>

<p><strong>입출력 예 #4</strong><br>
1단계에서 7단계까지 거치는 동안 new_id("123_.def")는 변하지 않습니다. 즉, new_id가 처음부터 카카오의 아이디 규칙에 맞습니다.</p>

<p><strong>입출력 예 #5</strong><br>
1단계 변화 없습니다.<br>
2단계 변화 없습니다.<br>
3단계 변화 없습니다.<br>
4단계 변화 없습니다.<br>
5단계 변화 없습니다.<br>
6단계 <code>"abcdefghijklmn.p"</code> → <code>"abcdefghijklmn."</code> → <code>"abcdefghijklmn"</code><br>
7단계 변화 없습니다.</p>
</div>
    </div>

---

# 카드 짝 맞추기

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>게임 개발자인 <code>베로니</code>는 개발 연습을 위해 다음과 같은 간단한 카드 짝맞추기 보드 게임을 개발해 보려고 합니다.<br>
게임이 시작되면 화면에는 카드 16장이 뒷면을 위로하여 <code>4 x 4</code> 크기의 격자 형태로 표시되어 있습니다. 각 카드의 앞면에는 카카오프렌즈 캐릭터 그림이 그려져 있으며, 8가지의 캐릭터 그림이 그려진 카드가 각기 2장씩 화면에 무작위로 배치되어 있습니다.<br>
유저가 카드를 2장 선택하여 앞면으로 뒤집었을 때 같은 그림이 그려진 카드면 해당 카드는 게임 화면에서 사라지며, 같은 그림이 아니라면 원래 상태로 뒷면이 보이도록 뒤집힙니다. 이와 같은 방법으로 모든 카드를 화면에서 사라지게 하면 게임이 종료됩니다.</p>

<p>게임에서 카드를 선택하는 방법은 다음과 같습니다.</p>

<ul>
<li>카드는 <code>커서</code>를 이용해서 선택할 수 있습니다.

<ul>
<li>커서는 4 x 4 화면에서 유저가 선택한 현재 위치를 표시하는 "굵고 빨간 테두리 상자"를 의미합니다.</li>
</ul></li>
<li>커서는 [Ctrl] 키와 방향키에 의해 이동되며 키 조작법은 다음과 같습니다.

<ul>
<li>방향키 ←, ↑, ↓, → 중 하나를 누르면, 커서가 누른 키 방향으로 1칸 이동합니다.</li>
<li>[Ctrl] 키를 누른 상태에서 방향키 ←, ↑, ↓, → 중 하나를 누르면, 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동합니다.

<ul>
<li>만약, 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동합니다.</li>
</ul></li>
<li>만약, 누른 키 방향으로 이동 가능한 카드 또는 빈 공간이 없어 이동할 수 없다면 커서는 움직이지 않습니다.</li>
</ul></li>
<li>커서가 위치한 카드를 뒤집기 위해서는 [Enter] 키를 입력합니다.

<ul>
<li>[Enter] 키를 입력해서 카드를 뒤집었을 때

<ul>
<li>앞면이 보이는 카드가 1장 뿐이라면 그림을 맞출 수 없으므로 두번째 카드를 뒤집을 때 까지 앞면을 유지합니다.</li>
<li>앞면이 보이는 카드가 2장이 된 경우, 두개의 카드에 그려진 그림이 같으면 해당 카드들이 화면에서 사라지며, 그림이 다르다면 두 카드 모두 뒷면이 보이도록 다시 뒤집힙니다.</li>
</ul></li>
</ul></li>
</ul>

<p>"베로니"는 게임 진행 중 카드의 짝을 맞춰 몇 장 제거된 상태에서 카드 앞면의 그림을 알고 있다면, 남은 카드를 모두 제거하는데 필요한 키 조작 횟수의 최솟값을 구해 보려고 합니다. 키 조작 횟수는 방향키와 [Enter] 키를 누르는 동작을 각각 조작 횟수 <code>1</code>로 계산하며, [Ctrl] 키와 방향키를 함께 누르는 동작 또한 조작 횟수 <code>1</code>로 계산합니다.</p>

<p>다음은 카드가 몇 장 제거된 상태의 게임 화면에서 커서를 이동하는 예시입니다.<br>
아래 그림에서 빈 칸은 이미 카드가 제거되어 없어진 칸을 의미하며, 그림이 그려진 칸은 카드 앞 면에 그려진 그림을 나타냅니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/bd1c06b3-6684-480a-85e6-53f1123b0770/2021_kakao_card_01.png" title="" alt="2021_kakao_card_01.png"><br>
예시에서 커서는 두번째 행, 첫번째 열 위치에서 시작하였습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8d9008a0-a933-44c7-92a8-96b701483d6e/2021_kakao_card_02.png" title="" alt="2021_kakao_card_02.png"><br>
[Enter] 입력, ↓ 이동, [Ctrl]+→ 이동, [Enter] 입력 = 키 조작 4회<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/89b256d7-b8a8-4fb1-a1f4-84407a029d03/2021_kakao_card_03.png" title="" alt="2021_kakao_card_03.png"><br>
[Ctrl]+↑ 이동, [Enter] 입력, [Ctrl]+← 이동, [Ctrl]+↓ 이동, [Enter] 입력 = 키 조작 5회<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/96b37dbd-bba1-47e0-89e5-7a3e518eab24/2021_kakao_card_04.png" title="" alt="2021_kakao_card_04.png"><br>
[Ctrl]+→ 이동, [Enter] 입력, [Ctrl]+↑ 이동, [Ctrl]+← 이동, [Enter] 입력 = 키 조작 5회</p>

<p>위와 같은 방법으로 커서를 이동하여 카드를 선택하고 그림을 맞추어 카드를 모두 제거하기 위해서는 총 14번(방향 이동 8번, [Enter] 키 입력 6번)의 키 조작 횟수가 필요합니다.</p>

<hr>

<h4><strong>[문제]</strong></h4>

<p>현재 카드가 놓인 상태를 나타내는 2차원 배열 board와 커서의 처음 위치 r, c가 매개변수로 주어질 때, 모든 카드를 제거하기 위한 키 조작 횟수의 최솟값을 return 하도록 solution 함수를 완성해 주세요.</p>

<h4><strong>[제한사항]</strong></h4>

<ul>
<li>board는 4 x 4 크기의 2차원 배열입니다.</li>
<li>board 배열의 각 원소는 0 이상 6 이하인 자연수입니다.

<ul>
<li>0은 카드가 제거된 빈 칸을 나타냅니다.</li>
<li>1 부터 6까지의 자연수는 2개씩 들어있으며 같은 숫자는 같은 그림의 카드를 의미합니다.</li>
<li>뒤집을 카드가 없는 경우(board의 모든 원소가 0인 경우)는 입력으로 주어지지 않습니다.</li>
</ul></li>
<li>r은 커서의 최초 세로(행) 위치를 의미합니다.</li>
<li>c는 커서의 최초 가로(열) 위치를 의미합니다.</li>
<li>r과 c는 0 이상 3 이하인 정수입니다.</li>
<li>게임 화면의 좌측 상단이 (0, 0), 우측 하단이 (3, 3) 입니다.</li>
</ul>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>board</th>
<th>r</th>
<th>c</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]</td>
<td>1</td>
<td>0</td>
<td>14</td>
</tr>
<tr>
<td>[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]</td>
<td>0</td>
<td>1</td>
<td>16</td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<hr>

<p><strong>입출력 예 #1</strong><br>
문제의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong><br>
입력으로 주어진 게임 화면은 아래 그림과 같습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/5c6e8d3f-2427-42b8-893b-5677cb45aa5d/2021_kakao_card_05.png" title="" alt="2021_kakao_card_05.png"></p>

<p>위 게임 화면에서 모든 카드를 제거하기 위한 키 조작 횟수의 최솟값은 16번 입니다.</p>
</div>
    </div>