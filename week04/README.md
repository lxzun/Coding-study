# 모의고사
<div class="guide-section" id="tour2" style="width: calc(40% - 12px);">

    <div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.</p>

<p>1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...<br>
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...<br>
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...</p>

<p>1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li>시험은 최대 10,000 문제로 구성되어있습니다.</li>
<li>문제의 정답은 1, 2, 3, 4, 5중 하나입니다.</li>
<li>가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>answers</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1,2,3,4,5]</td>
<td>[1]</td>
</tr>
<tr>
<td>[1,3,2,4,2]</td>
<td>[1,2,3]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>수포자 1은 모든 문제를 맞혔습니다.</li>
<li>수포자 2는 모든 문제를 틀렸습니다.</li>
<li>수포자 3은 모든 문제를 틀렸습니다.</li>
</ul>

<p>따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.</p>

<p>입출력 예 #2</p>

<ul>
<li>모든 사람이 2문제씩을 맞췄습니다.</li>
</ul>
</div>
    </div>

  </div>

# 소수 찾기

<div class="guide-section" id="tour2" style="width: calc(40% - 12px);">

    <div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.</p>

<p>각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>numbers는 길이 1 이상 7 이하인 문자열입니다.</li>
<li>numbers는 0~9까지 숫자만으로 이루어져 있습니다.</li>
<li>"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>"17"</td>
<td>3</td>
</tr>
<tr>
<td>"011"</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제 #1<br>
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.</p>

<p>예제 #2<br>
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.</p>

<ul>
<li>11과 011은 같은 숫자로 취급합니다.</li>
</ul>

<p><a href="http://2009.nwerc.eu/results/nwerc09.pdf" target="_blank" rel="noopener">출처</a></p>
</div>
    </div>

  </div>

# 카펫

<div class="guide-section" id="tour2" style="width: calc(40% - 12px);">

    <div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b1ebb809-f333-4df2-bc81-02682900dc2d/carpet.png" width="40%" title="" alt="carpet.png"></p>

<p>Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.</p>

<p>Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.</li>
<li>노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.</li>
<li>카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>brown</th>
<th>yellow</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>2</td>
<td>[4, 3]</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>[3, 3]</td>
</tr>
<tr>
<td>24</td>
<td>24</td>
<td>[8, 6]</td>
</tr>
</tbody>
      </table>
<p><a href="http://hsin.hr/coci/archive/2010_2011/contest4_tasks.pdf" target="_blank" rel="noopener">출처</a></p>

<p>※ 공지 - 2020년 2월 3일 테스트케이스가 추가되었습니다.<br>
※ 공지 - 2020년 5월 11일 웹접근성을 고려하여 빨간색을 노란색으로 수정하였습니다.</p>
</div>
    </div>

  </div>