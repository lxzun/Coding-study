# [**신고 결과 받기**](https://programmers.co.kr/learn/courses/30/lessons/92334)

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><h5>문제 설명</h5>

<p>신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.</p>

<ul>
<li>각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.

<ul>
<li>신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.</li>
<li>한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.</li>
</ul></li>
<li>k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.

<ul>
<li>유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.</li>
</ul></li>
</ul>

<p>다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.</p>
<table class="table">
        <thead><tr>
<th>유저 ID</th>
<th>유저가 신고한 ID</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>"muzi"</td>
<td>"frodo"</td>
<td>"muzi"가 "frodo"를 신고했습니다.</td>
</tr>
<tr>
<td>"apeach"</td>
<td>"frodo"</td>
<td>"apeach"가 "frodo"를 신고했습니다.</td>
</tr>
<tr>
<td>"frodo"</td>
<td>"neo"</td>
<td>"frodo"가 "neo"를 신고했습니다.</td>
</tr>
<tr>
<td>"muzi"</td>
<td>"neo"</td>
<td>"muzi"가 "neo"를 신고했습니다.</td>
</tr>
<tr>
<td>"apeach"</td>
<td>"muzi"</td>
<td>"apeach"가 "muzi"를 신고했습니다.</td>
</tr>
</tbody>
      </table>
<p>각 유저별로 신고당한 횟수는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>유저 ID</th>
<th>신고당한 횟수</th>
</tr>
</thead>
        <tbody><tr>
<td>"muzi"</td>
<td>1</td>
</tr>
<tr>
<td>"frodo"</td>
<td>2</td>
</tr>
<tr>
<td>"apeach"</td>
<td>0</td>
</tr>
<tr>
<td>"neo"</td>
<td>2</td>
</tr>
</tbody>
      </table>
<p>위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>유저 ID</th>
<th>유저가 신고한 ID</th>
<th>정지된 ID</th>
</tr>
</thead>
        <tbody><tr>
<td>"muzi"</td>
<td>["frodo", "neo"]</td>
<td>["frodo", "neo"]</td>
</tr>
<tr>
<td>"frodo"</td>
<td>["neo"]</td>
<td>["neo"]</td>
</tr>
<tr>
<td>"apeach"</td>
<td>["muzi", "frodo"]</td>
<td>["frodo"]</td>
</tr>
<tr>
<td>"neo"</td>
<td>없음</td>
<td>없음</td>
</tr>
</tbody>
      </table>
<p>따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.</p>

<p>이용자의 ID가 담긴 문자열 배열 <code>id_list</code>, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 <code>report</code>, 정지 기준이 되는 신고 횟수 <code>k</code>가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>id_list</code>의 길이 ≤ 1,000

<ul>
<li>1 ≤ <code>id_list</code>의 원소 길이 ≤ 10</li>
<li><code>id_list</code>의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.</li>
<li><code>id_list</code>에는 같은 아이디가 중복해서 들어있지 않습니다.</li>
</ul></li>
<li>1 ≤ <code>report</code>의 길이 ≤ 200,000

<ul>
<li>3 ≤ <code>report</code>의 원소 길이 ≤ 21</li>
<li><code>report</code>의 원소는 "이용자id 신고한id"형태의 문자열입니다.</li>
<li>예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.</li>
<li>id는 알파벳 소문자로만 이루어져 있습니다.</li>
<li>이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.</li>
<li>자기 자신을 신고하는 경우는 없습니다.</li>
</ul></li>
<li>1 ≤ <code>k</code> ≤ 200, <code>k</code>는 자연수입니다.</li>
<li>return 하는 배열은 <code>id_list</code>에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>id_list</th>
<th>report</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>["muzi", "frodo", "apeach", "neo"]</code></td>
<td><code>["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]</code></td>
<td>2</td>
<td>[2,1,1,0]</td>
</tr>
<tr>
<td><code>["con", "ryan"]</code></td>
<td><code>["ryan con", "ryan con", "ryan con", "ryan con"]</code></td>
<td>3</td>
<td>[0,0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>"ryan"이 "con"을 4번 신고했으나, 주어진 조건에 따라 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리합니다. 따라서 "con"은 1회 신고당했습니다. 3번 이상 신고당한 이용자는 없으며, "con"과 "ryan"은 결과 메일을 받지 않습니다. 따라서 [0, 0]을 return 합니다.</p>

<hr>

<h5>제한시간 안내</h5>

<ul>
<li>정확성 테스트 : 10초</li>
</ul>
</div>
    </div>

# [**주차 요금 계산**](https://programmers.co.kr/learn/courses/30/lessons/92341)

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><h5>문제 설명</h5>

<p>주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.</p>

<ul>
<li><strong>요금표</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>기본 시간(분)</th>
<th>기본 요금(원)</th>
<th>단위 시간(분)</th>
<th>단위 요금(원)</th>
</tr>
</thead>
        <tbody><tr>
<td>180</td>
<td>5000</td>
<td>10</td>
<td>600</td>
</tr>
</tbody>
      </table>
<p>&nbsp;</p>

<ul>
<li><strong>입/출차 기록</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>시각(시:분)</th>
<th>차량 번호</th>
<th>내역</th>
</tr>
</thead>
        <tbody><tr>
<td>05:34</td>
<td>5961</td>
<td>입차</td>
</tr>
<tr>
<td>06:00</td>
<td>0000</td>
<td>입차</td>
</tr>
<tr>
<td>06:34</td>
<td>0000</td>
<td>출차</td>
</tr>
<tr>
<td>07:59</td>
<td>5961</td>
<td>출차</td>
</tr>
<tr>
<td>07:59</td>
<td>0148</td>
<td>입차</td>
</tr>
<tr>
<td>18:59</td>
<td>0000</td>
<td>입차</td>
</tr>
<tr>
<td>19:09</td>
<td>0148</td>
<td>출차</td>
</tr>
<tr>
<td>22:59</td>
<td>5961</td>
<td>입차</td>
</tr>
<tr>
<td>23:00</td>
<td>5961</td>
<td>출차</td>
</tr>
</tbody>
      </table>
<p>&nbsp;</p>

<ul>
<li><strong>자동차별 주차 요금</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>차량 번호</th>
<th>누적 주차 시간(분)</th>
<th>주차 요금(원)</th>
</tr>
</thead>
        <tbody><tr>
<td>0000</td>
<td>34 + 300 = 334</td>
<td>5000 + <code>⌈</code>(334 - 180) / 10<code>⌉</code> x 600 = 14600</td>
</tr>
<tr>
<td>0148</td>
<td>670</td>
<td>5000 +<code>⌈</code>(670 - 180) / 10<code>⌉</code>x 600 = 34400</td>
</tr>
<tr>
<td>5961</td>
<td>145 + 1 = 146</td>
<td>5000</td>
</tr>
</tbody>
      </table>
<ul>
<li>어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.

<ul>
<li><code>0000</code>번 차량은 18:59에 입차된 이후, 출차된 내역이 없습니다. 따라서, 23:59에 출차된 것으로 간주합니다.</li>
</ul></li>
<li>00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다. </li>
<li>누적 주차 시간이 <code>기본 시간</code>이하라면, <code>기본 요금</code>을 청구합니다.<br></li>
<li>누적 주차 시간이 <code>기본 시간</code>을 초과하면, <code>기본 요금</code>에 더해서, 초과한 시간에 대해서 <code>단위 시간</code> 마다 <code>단위 요금</code>을 청구합니다.

<ul>
<li>초과한 시간이 <code>단위 시간</code>으로 나누어 떨어지지 않으면, <code>올림</code>합니다.<br></li>
<li><code>⌈</code>a<code>⌉</code> : a보다 작지 않은 최소의 정수를 의미합니다. 즉, <code>올림</code>을 의미합니다.</li>
</ul></li>
</ul>

<p>주차 요금을 나타내는 정수 배열 <code>fees</code>, 자동차의 입/출차 내역을 나타내는 문자열 배열 <code>records</code>가 매개변수로 주어집니다. <strong>차량 번호가 작은 자동차부터</strong> 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li><p><code>fees</code>의 길이 = 4</p>

<ul>
<li>fees[0] = <code>기본 시간(분)</code></li>
<li>1 ≤ fees[0] ≤ 1,439 </li>
<li>fees[1] = <code>기본 요금(원)</code></li>
<li>0 ≤ fees[1] ≤ 100,000</li>
<li>fees[2] = <code>단위 시간(분)</code></li>
<li>1 ≤ fees[2] ≤ 1,439</li>
<li>fees[3] = <code>단위 요금(원)</code> </li>
<li>1 ≤ fees[3] ≤ 10,000</li>
</ul></li>
<li><p>1 ≤ <code>records</code>의 길이 ≤ 1,000</p>

<ul>
<li><code>records</code>의 각 원소는 <code>"시각 차량번호 내역"</code> 형식의 문자열입니다.</li>
<li><code>시각</code>, <code>차량번호</code>, <code>내역</code>은 하나의 공백으로 구분되어 있습니다.</li>
<li><code>시각</code>은 차량이 입차되거나 출차된 시각을 나타내며, <code>HH:MM</code> 형식의 길이 5인 문자열입니다.

<ul>
<li><code>HH:MM</code>은 00:00부터 23:59까지 주어집니다.</li>
<li>잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.</li>
</ul></li>
<li><code>차량번호</code>는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열입니다.<br></li>
<li><code>내역</code>은 길이 2 또는 3인 문자열로, <code>IN</code> 또는 <code>OUT</code>입니다. <code>IN</code>은 입차를, <code>OUT</code>은 출차를 의미합니다. </li>
<li><code>records</code>의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.</li>
<li><code>records</code>는 하루 동안의 입/출차된 기록만 담고 있으며, 입차된 차량이 다음날 출차되는 경우는 입력으로 주어지지 않습니다.</li>
<li>같은 시각에, 같은 차량번호의 내역이 2번 이상 나타내지 않습니다.</li>
<li>마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.</li>
<li>아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.

<ul>
<li>주차장에 없는 차량이 출차되는 경우</li>
<li>주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우</li>
</ul></li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>fees</th>
<th>records</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[180, 5000, 10, 600]</td>
<td><code>["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]</code></td>
<td>[14600, 34400, 5000]</td>
</tr>
<tr>
<td>[120, 0, 60, 591]</td>
<td><code>["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]</code></td>
<td>[0, 591]</td>
</tr>
<tr>
<td>[1, 461, 1, 10]</td>
<td><code>["00:00 1234 IN"]</code></td>
<td>[14841]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li><strong>요금표</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>기본 시간(분)</th>
<th>기본 요금(원)</th>
<th>단위 시간(분)</th>
<th>단위 요금(원)</th>
</tr>
</thead>
        <tbody><tr>
<td>120</td>
<td>0</td>
<td>60</td>
<td>591</td>
</tr>
</tbody>
      </table>
<p>&nbsp;</p>

<ul>
<li><strong>입/출차 기록</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>시각(시:분)</th>
<th>차량 번호</th>
<th>내역</th>
</tr>
</thead>
        <tbody><tr>
<td>16:00</td>
<td>3961</td>
<td>입차</td>
</tr>
<tr>
<td>16:00</td>
<td>0202</td>
<td>입차</td>
</tr>
<tr>
<td>18:00</td>
<td>3961</td>
<td>출차</td>
</tr>
<tr>
<td>18:00</td>
<td>0202</td>
<td>출차</td>
</tr>
<tr>
<td>23:58</td>
<td>3961</td>
<td>입차</td>
</tr>
</tbody>
      </table>
<p>&nbsp;</p>

<ul>
<li><strong>자동차별 주차 요금</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>차량 번호</th>
<th>누적 주차 시간(분)</th>
<th>주차 요금(원)</th>
</tr>
</thead>
        <tbody><tr>
<td>0202</td>
<td>120</td>
<td>0</td>
</tr>
<tr>
<td>3961</td>
<td>120 + 1 = 121</td>
<td>0 +<code>⌈</code>(121 - 120) / 60<code>⌉</code>x 591 = 591</td>
</tr>
</tbody>
      </table>
<ul>
<li><code>3961</code>번 차량은 2번째 입차된 후에는 출차된 내역이 없으므로, 23:59에 출차되었다고 간주합니다. </li>
</ul>

<p>&nbsp;</p>

<p><strong>입출력 예 #3</strong></p>

<ul>
<li><strong>요금표</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>기본 시간(분)</th>
<th>기본 요금(원)</th>
<th>단위 시간(분)</th>
<th>단위 요금(원)</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>461</td>
<td>1</td>
<td>10</td>
</tr>
</tbody>
      </table>
<p>&nbsp;</p>

<ul>
<li><strong>입/출차 기록</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>시각(시:분)</th>
<th>차량 번호</th>
<th>내역</th>
</tr>
</thead>
        <tbody><tr>
<td>00:00</td>
<td>1234</td>
<td>입차</td>
</tr>
</tbody>
      </table>
<p>&nbsp;</p>

<ul>
<li><strong>자동차별 주차 요금</strong></li>
</ul>
<table class="table">
        <thead><tr>
<th>차량 번호</th>
<th>누적 주차 시간(분)</th>
<th>주차 요금(원)</th>
</tr>
</thead>
        <tbody><tr>
<td>1234</td>
<td>1439</td>
<td>461 +<code>⌈</code>(1439 - 1) / 1<code>⌉</code>x 10 = 14841</td>
</tr>
</tbody>
      </table>
<ul>
<li><code>1234</code>번 차량은 출차 내역이 없으므로, 23:59에 출차되었다고 간주합니다.</li>
</ul>

<hr>

<p>​</p>

<h5>제한시간 안내</h5>

<ul>
<li>정확성 테스트 : 10초</li>
</ul>
</div>
    </div>

# [**양과 늑대**](https://programmers.co.kr/learn/courses/30/lessons/92343)

<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><h5>문제 설명</h5>

<p>2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있습니다. 이 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다. 각 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다. 이때, 늑대는 양을 잡아먹을 기회를 노리고 있으며, 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다. 당신은 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ed7118a9-a99b-4f3a-9779-a94816529e78/03_2022_%E1%84%80%E1%85%A9%E1%86%BC%E1%84%8E%E1%85%A2%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6_%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%80%E1%85%AA%E1%84%82%E1%85%B3%E1%86%A8%E1%84%83%E1%85%A2_01.png" title="" alt="03_2022_공채문제_양과늑대_01.png"></p>

<p>예를 들어, 위 그림의 경우(루트 노드에는 항상 양이 있습니다) 0번 노드(루트 노드)에서 출발하면 양을 한마리 모을 수 있습니다. 다음으로 1번 노드로 이동하면 당신이 모은 양은 두 마리가 됩니다. 이때, 바로 4번 노드로 이동하면 늑대 한 마리가 당신을 따라오게 됩니다. 아직은 양 2마리, 늑대 1마리로 양이 잡아먹히지 않지만, 이후에 갈 수 있는 아직 방문하지 않은 모든 노드(2, 3, 6, 8번)에는 늑대가 있습니다. 이어서 늑대가 있는 노드로 이동한다면(예를 들어 바로 6번 노드로 이동한다면) 양 2마리, 늑대 2마리가 되어 양이 모두 잡아먹힙니다. 여기서는 0번, 1번 노드를 방문하여 양을 2마리 모은 후, 8번 노드로 이동한 후(양 2마리 늑대 1마리) 이어서 7번, 9번 노드를 방문하면 양 4마리 늑대 1마리가 됩니다. 이제 4번, 6번 노드로 이동하면 양 4마리, 늑대 3마리가 되며, 이제 5번 노드로 이동할 수 있게 됩니다. 따라서 양을 최대 5마리 모을 수 있습니다. </p>

<p>각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 <code>info</code>, 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 <code>edges</code>가 매개변수로 주어질 때, 문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리인지 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>info</code>의 길이 ≤ 17

<ul>
<li><code>info</code>의 원소는 0 또는 1 입니다.</li>
<li>info[i]는 i번 노드에 있는 양 또는 늑대를 나타냅니다.</li>
<li>0은 양, 1은 늑대를 의미합니다.</li>
<li>info[0]의 값은 항상 0입니다. 즉, 0번 노드(루트 노드)에는 항상 양이 있습니다.</li>
</ul></li>
<li><code>edges</code>의 세로(행) 길이 = <code>info</code>의 길이 - 1

<ul>
<li><code>edges</code>의 가로(열) 길이 = 2</li>
<li><code>edges</code>의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태로, 서로 연결된 두 노드를 나타냅니다.</li>
<li>동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.</li>
<li>항상 하나의 이진 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.</li>
<li>0번 노드는 항상 루트 노드입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>info</th>
<th>edges</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[0,0,1,1,1,0,1,0,1,0,1,1]</td>
<td>[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]</td>
<td>5</td>
</tr>
<tr>
<td>[0,1,0,1,1,0,1,0,0,1,0]</td>
<td>[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]</td>
<td>5</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>주어진 입력은 다음 그림과 같습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/32656ee0-814e-4dd9-93a3-abed1ce31ec1/03_2022_%E1%84%80%E1%85%A9%E1%86%BC%E1%84%8E%E1%85%A2%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6_%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%80%E1%85%AA%E1%84%82%E1%85%B3%E1%86%A8%E1%84%83%E1%85%A2_02.png" title="" alt="03_2022_공채문제_양과늑대_02.png"></p>

<p>0번 - 2번 - 5번 - 1번 - 4번 - 8번 - 3번 - 7번 노드 순으로 이동하면 양 5마리 늑대 3마리가 됩니다. 여기서 6번, 9번 노드로 이동하면 양 5마리, 늑대 5마리가 되어 양이 모두 잡아먹히게 됩니다. 따라서 늑대에게 잡아먹히지 않도록 하면서 최대로 모을 수 있는 양은 5마리입니다.</p>

<hr>

<h5>제한시간 안내</h5>

<ul>
<li>정확성 테스트 : 10초</li>
</ul>
</div>
    </div>