# 프린터
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.</p>
<div class="highlight"><pre class="codehilite"><code>1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
</code></pre></div>
<p>예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.</p>

<p>내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.</p>

<p>현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.</li>
<li>인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.</li>
<li>location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>priorities</th>
<th>location</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[2, 1, 3, 2]</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>[1, 1, 9, 1, 1, 1]</td>
<td>0</td>
<td>5</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>예제 #1</p>

<p>문제에 나온 예와 같습니다.</p>

<p>예제 #2</p>

<p>6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다. </p>

<p><a href="http://www.csc.kth.se/contest/nwerc/2006/problems/nwerc06.pdf" target="_blank" rel="noopener">출처</a></p>
</div>
    </div>

---
# 주식 가격
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한사항</h5>

<ul>
<li>prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.</li>
<li>prices의 길이는 2 이상 100,000 이하입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>prices</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 2, 3, 2, 3]</td>
<td>[4, 3, 1, 1, 0]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<ul>
<li>1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.</li>
<li>2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.</li>
<li>3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.</li>
<li>4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.</li>
<li>5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.</li>
</ul>

<p>※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.</p>
</div>
    </div>