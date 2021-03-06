# 순위 검색
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p><strong>[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]</strong></p>

<p>카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다. 이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.</p>

<ul>
<li>코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.</li>
<li>지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.</li>
<li>지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.</li>
<li>선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.</li>
</ul>

<p>인재영입팀에 근무하고 있는 <code>니니즈</code>는 코딩테스트 결과를 분석하여 채용에 참여한 개발팀들에 제공하기 위해 지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.<br>
예를 들어, 개발팀에서 궁금해하는 문의사항은 다음과 같은 형태가 될 수 있습니다.<br>
<code>코딩테스트에 java로 참여했으며, backend 직군을 선택했고, junior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?</code></p>

<p>물론 이 외에도 각 개발팀의 상황에 따라 아래와 같이 다양한 형태의 문의가 있을 수 있습니다.</p>

<ul>
<li>코딩테스트에 python으로 참여했으며, frontend 직군을 선택했고, senior 경력이면서, 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?</li>
<li>코딩테스트에 cpp로 참여했으며, senior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?</li>
<li>backend 직군을 선택했고, senior 경력이면서 코딩테스트 점수를 200점 이상 받은 사람은 모두 몇 명인가? </li>
<li>소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 250점 이상 받은 사람은 모두 몇 명인가?</li>
<li>코딩테스트 점수를 150점 이상 받은 사람은 모두 몇 명인가?</li>
</ul>

<p>즉, 개발팀에서 궁금해하는 내용은 다음과 같은 형태를 갖습니다.</p>
<div class="highlight"><pre class="codehilite"><code>* [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
</code></pre></div>
<hr>

<h4><strong>[문제]</strong></h4>

<p>지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info, 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,<br>
각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.</p>

<h4><strong>[제한사항]</strong></h4>

<ul>
<li>info 배열의 크기는 1 이상 50,000 이하입니다.</li>
<li>info 배열 각 원소의 값은 지원자가 지원서에 입력한 4가지 값과 코딩테스트 점수를 합친 "개발언어 직군 경력 소울푸드 점수" 형식입니다.

<ul>
<li>개발언어는 cpp, java, python 중 하나입니다.</li>
<li>직군은 backend, frontend 중 하나입니다.</li>
<li>경력은 junior, senior 중 하나입니다.</li>
<li>소울푸드는 chicken, pizza 중 하나입니다.</li>
<li>점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.</li>
<li>각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.</li>
</ul></li>
<li>query 배열의 크기는 1 이상 100,000 이하입니다.</li>
<li>query의 각 문자열은 "[조건] X" 형식입니다.

<ul>
<li>[조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.</li>
<li>언어는 cpp, java, python, - 중 하나입니다.</li>
<li>직군은 backend, frontend, - 중 하나입니다.</li>
<li>경력은 junior, senior, - 중 하나입니다.</li>
<li>소울푸드는 chicken, pizza, - 중 하나입니다.</li>
<li>'-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.</li>
<li>X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.</li>
<li>각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.</li>
<li>예를 들면, "cpp and - and senior and pizza 500"은 "cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?"를 의미합니다.</li>
</ul></li>
</ul>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>info</th>
<th>query</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]</code></td>
<td><code>["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]</code></td>
<td>[1,1,1,1,2,4]</td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<p>지원자 정보를 표로 나타내면 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>언어</th>
<th>직군</th>
<th>경력</th>
<th>소울 푸드</th>
<th>점수</th>
</tr>
</thead>
        <tbody><tr>
<td>java</td>
<td>backend</td>
<td>junior</td>
<td>pizza</td>
<td>150</td>
</tr>
<tr>
<td>python</td>
<td>frontend</td>
<td>senior</td>
<td>chicken</td>
<td>210</td>
</tr>
<tr>
<td>python</td>
<td>frontend</td>
<td>senior</td>
<td>chicken</td>
<td>150</td>
</tr>
<tr>
<td>cpp</td>
<td>backend</td>
<td>senior</td>
<td>pizza</td>
<td>260</td>
</tr>
<tr>
<td>java</td>
<td>backend</td>
<td>junior</td>
<td>chicken</td>
<td>80</td>
</tr>
<tr>
<td>python</td>
<td>backend</td>
<td>senior</td>
<td>chicken</td>
<td>50</td>
</tr>
</tbody>
      </table>
<ul>
<li><code>"java and backend and junior and pizza 100"</code> : java로 코딩테스트를 봤으며, backend 직군을 선택했고 junior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 100점 이상 받은 지원자는 1명 입니다.</li>
<li><code>"python and frontend and senior and chicken 200"</code> : python으로 코딩테스트를 봤으며, frontend 직군을 선택했고, senior 경력이면서 소울 푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 200점 이상 받은 지원자는 1명 입니다.</li>
<li><code>"cpp and - and senior and pizza 250"</code> : cpp로 코딩테스트를 봤으며, senior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 250점 이상 받은 지원자는 1명 입니다.</li>
<li><code>"- and backend and senior and - 150"</code> : backend 직군을 선택했고, senior 경력인 지원자 중 코딩테스트 점수를 150점 이상 받은 지원자는 1명 입니다.</li>
<li><code>"- and - and - and chicken 100"</code> : 소울푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 100점 이상을 받은 지원자는 2명 입니다.</li>
<li><code>"- and - and - and - 150"</code> : 코딩테스트 점수를 150점 이상 받은 지원자는 4명 입니다.</li>
</ul>
</div>
    </div>

---

# 광고 삽입
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p><code>카카오TV</code>에서 유명한 크리에이터로 활동 중인 <code>죠르디</code>는 환경 단체로부터 자신의 가장 인기있는 동영상에 지구온난화의 심각성을 알리기 위한 공익광고를 넣어 달라는 요청을 받았습니다. 평소에 환경 문제에 관심을 가지고 있던 "죠르디"는 요청을 받아들였고 광고효과를 높이기 위해 시청자들이 가장 많이 보는 구간에 공익광고를 넣으려고 합니다. "죠르디"는 시청자들이 해당 동영상의 어떤 구간을 재생했는 지 알 수 있는 재생구간 기록을 구했고, 해당 기록을 바탕으로 공익광고가 삽입될 최적의 위치를 고를 수 있었습니다.<br>
참고로 광고는 재생 중인 동영상의 오른쪽 아래에서 원래 영상과 <code>동시에 재생되는</code> PIP(Picture in Picture) 형태로 제공됩니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/597ec277-4451-4289-8817-2970be644a69/2021_kakao_cf_01.png" title="" alt="2021_kakao_cf_01.png"></p>

<p>다음은 "죠르디"가 공익광고가 삽입될 최적의 위치를 고르는 과정을 그림으로 설명한 것입니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e733fafb-1e6b-4d30-bbab-a22f366229e7/2021_kakao_cf_02.png" title="" alt="2021_kakao_cf_02.png"></p>

<ul>
<li>그림의 파란색 선은 광고를 검토 중인 "죠르디" 동영상의 전체 재생 구간을 나타냅니다.

<ul>
<li>위 그림에서, "죠르디" 동영상의 총 재생시간은 <code>02시간 03분 55초</code> 입니다.</li>
</ul></li>
<li>그림의 검은색 선들은 각 시청자들이 "죠르디"의 동영상을 재생한 구간의 위치를 표시하고 있습니다.

<ul>
<li>검은색 선의 가운데 숫자는 각 재생 기록을 구분하는 ID를 나타냅니다.</li>
<li>검은색 선에 표기된 왼쪽 끝 숫자와 오른쪽 끝 숫자는 시청자들이 재생한 동영상 구간의 시작 시각과 종료 시각을 나타냅니다.</li>
<li>위 그림에서, 3번 재생 기록은 <code>00시 25분 50초</code> 부터 <code>00시 48분 29초</code> 까지 총 <code>00시간 22분 39초</code> 동안 죠르디의 동영상을 재생했습니다. <sup id="fnref1"><a href="#fn1">1</a></sup></li>
<li>위 그림에서, 1번 재생 기록은 <code>01시 20분 15초</code> 부터 <code>01시 45분 14초</code> 까지 총 <code>00시간 24분 59초</code> 동안 죠르디의 동영상을 재생했습니다.</li>
</ul></li>
<li>그림의 빨간색 선은 "죠르디"가 선택한 최적의 공익광고 위치를 나타냅니다.

<ul>
<li>만약 공익광고의 재생시간이 <code>00시간 14분 15초</code>라면, 위의 그림처럼 <code>01시 30분 59초</code> 부터 <code>01시 45분 14초</code> 까지 공익광고를 삽입하는 것이 가장 좋습니다. 이 구간을 시청한 시청자들의 누적 재생시간이 가장 크기 때문입니다.</li>
<li><code>01시 30분 59초</code> 부터 <code>01시 45분 14초</code> 까지의 누적 재생시간은 다음과 같이 계산됩니다.

<ul>
<li><code>01시 30분 59초</code> 부터 <code>01시 37분 44초</code> 까지 : 4번, 1번 재생 기록이 두차례 있으므로 재생시간의 합은 <code>00시간 06분 45초</code> X 2 = <code>00시간 13분 30초</code></li>
<li><code>01시 37분 44초</code> 부터 <code>01시 45분 14초</code> 까지 : 4번, 1번, 5번 재생 기록이 세차례 있으므로 재생시간의 합은 <code>00시간 07분 30초</code> X 3 = <code>00시간 22분 30초</code></li>
<li>따라서, 이 구간 시청자들의 누적 재생시간은 <code>00시간 13분 30초</code> + <code>00시간 22분 30초</code> = <code>00시간 36분 00초</code>입니다.</li>
</ul></li>
</ul></li>
</ul>

<hr>

<h4><strong>[문제]</strong></h4>

<p>"죠르디"의 동영상 재생시간 길이 play_time, 공익광고의 재생시간 길이 adv_time, 시청자들이 해당 동영상을 재생했던 구간 정보 logs가 매개변수로 주어질 때, 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려고 합니다. 이때, 공익광고가 들어갈 <code>시작 시각</code>을 구해서 return 하도록 solution 함수를 완성해주세요. 만약, 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면, 그 중에서 <code>가장 빠른 시작 시각</code>을 return 하도록 합니다.</p>

<h4><strong>[제한사항]</strong></h4>

<ul>
<li>play_time, adv_time은 길이 8로 고정된 문자열입니다.

<ul>
<li>play_time, adv_time은 <code>HH:MM:SS</code> 형식이며, <code>00:00:01</code> 이상 <code>99:59:59</code> 이하입니다.</li>
<li>즉, 동영상 재생시간과 공익광고 재생시간은 <code>00시간 00분 01초</code> 이상 <code>99시간 59분 59초</code> 이하입니다.</li>
<li>공익광고 재생시간은 동영상 재생시간보다 짧거나 같게 주어집니다.</li>
</ul></li>
<li><p>logs는 크기가 1 이상 300,000 이하인 문자열 배열입니다.</p>

<ul>
<li>logs 배열의 각 원소는 시청자의 재생 구간을 나타냅니다.</li>
<li>logs 배열의 각 원소는 길이가 17로 고정된 문자열입니다.</li>
<li>logs 배열의 각 원소는 <code>H1:M1:S1-H2:M2:S2</code> 형식입니다.

<ul>
<li><code>H1:M1:S1</code>은 동영상이 시작된 시각, <code>H2:M2:S2</code>는 동영상이 종료된 시각을 나타냅니다.</li>
<li><code>H1:M1:S1</code>는 <code>H2:M2:S2</code>보다 1초 이상 이전 시각으로 주어집니다.</li>
<li><code>H1:M1:S1</code>와 <code>H2:M2:S2</code>는 play_time 이내의 시각입니다.</li>
</ul></li>
</ul></li>
<li><p>시간을 나타내는 <code>HH, H1, H2</code>의 범위는 00~99, 분을 나타내는 <code>MM, M1, M2</code>의 범위는  00~59, 초를 나타내는 <code>SS, S1, S2</code>의 범위는 00~59까지 사용됩니다. 잘못된 시각은 입력으로 주어지지 않습니다. (예: <code>04:60:24</code>, <code>11:12:78</code>, <code>123:12:45</code> 등)</p></li>
<li><p>return 값의 형식</p>

<ul>
<li>공익광고를 삽입할 시각을 <code>HH:MM:SS</code> 형식의 8자리 문자열로 반환합니다.</li>
</ul></li>
</ul>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>play_time</th>
<th>adv_time</th>
<th>logs</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>"02:03:55"</code></td>
<td><code>"00:14:15"</code></td>
<td><code>["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]</code></td>
<td><code>"01:30:59"</code></td>
</tr>
<tr>
<td><code>"99:59:59"</code></td>
<td><code>"25:00:00"</code></td>
<td><code>["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]</code></td>
<td><code>"01:00:00"</code></td>
</tr>
<tr>
<td><code>"50:00:00"</code></td>
<td><code>"50:00:00"</code></td>
<td><code>["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]</code></td>
<td><code>"00:00:00"</code></td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<hr>

<p><strong>입출력 예 #1</strong><br>
문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0e58c7f5-2b81-43f2-95e1-c504f17aab9b/2021_kakao_cf_03.png" title="" alt="2021_kakao_cf_03.png"></p>

<p><code>01:00:00</code>에 공익광고를 삽입하면 <code>26:00:00</code>까지 재생되며, 이곳이 가장 좋은 위치입니다. 이 구간의 시청자 누적 재생시간은 다음과 같습니다.</p>

<ul>
<li><code>01:00:00-11:00:00</code> : 해당 구간이 1회(2번 기록) 재생되었으므로 누적 재생시간은 <code>10시간 00분 00초</code> 입니다.</li>
<li><code>11:00:00-21:00:00</code> : 해당 구간이 2회(2번, 4번 기록) 재생되었으므로 누적 재생시간은 <code>20시간 00분 00초</code> 입니다.</li>
<li><code>21:00:00-26:00:00</code> : 해당 구간이 1회(4번 기록) 재생되었으므로 누적 재생시간은 <code>05시간 00분 00초</code> 입니다.</li>
<li>따라서, 이 구간의 시청자 누적 재생시간은 <code>10시간 00분 00초</code> + <code>20시간 00분 00초</code> + <code>05시간 00분 00초</code> = <code>35시간 00분 00초</code> 입니다.</li>
<li>초록색으로 표시된 구간(<code>69:59:59-94:59:59</code>)에 광고를 삽입해도 동일한 결과를 얻을 수 있으나, <code>01:00:00</code>이 <code>69:59:59</code> 보다 빠른 시각이므로, <code>"01:00:00"</code>을 return 합니다.</li>
</ul>

<p><strong>입출력 예 #3</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8e564c82-00ce-4e1a-80fc-5cd96e465a69/2021_kakao_cf_04.png" title="" alt="2021_kakao_cf_04.png"></p>

<p>동영상 재생시간과 공익광고 재생시간이 같으므로, 삽입할 수 있는 위치는 맨 처음(<code>00:00:00</code>)이 유일합니다.</p>

<div class="footnotes">
<hr>
<ol>

<li id="fn1">
<p><code>동영상 재생시간 = 재생이 종료된 시각 - 재생이 시작된 시각</code>(예를 들어, <code>00시 00분 01초</code>부터 <code>00시 00분 10초</code>까지 동영상이 재생되었다면, 동영상 재생시간은 <code>9초</code> 입니다.)&nbsp;<a href="#fnref1">↩</a></p>
</li>

</ol>
</div>
</div>
    </div>
