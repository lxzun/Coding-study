# [**1935. Maximum Number of Words You Can Type**](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)

<div class="content__u3I1 question-content__JfgR"><div><p>There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.</p>

<p>Given a string <code>text</code> of words separated by a single space (no leading or trailing spaces) and a string <code>brokenLetters</code> of all <strong>distinct</strong> letter keys that are broken, return <em>the <strong>number of words</strong> in</em> <code>text</code> <em>you can fully type using this keyboard</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> text = "hello world", brokenLetters = "ad"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We cannot type "world" because the 'd' key is broken.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> text = "leet code", brokenLetters = "lt"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We cannot type "leet" because the 'l' and 't' keys are broken.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> text = "leet code", brokenLetters = "e"
<strong>Output:</strong> 0
<strong>Explanation:</strong> We cannot type either word because the 'e' key is broken.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= brokenLetters.length &lt;= 26</code></li>
	<li><code>text</code> consists of words separated by a single space without any leading or trailing spaces.</li>
	<li>Each word only consists of lowercase English letters.</li>
	<li><code>brokenLetters</code> consists of <strong>distinct</strong> lowercase English letters.</li>
</ul>
</div></div><br>

---

<br>

# [**1348. Tweet Counts Per Frequency**](https://leetcode.com/problems/tweet-counts-per-frequency/)

<div class="content__u3I1 question-content__JfgR"><div><p>A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller <strong>time chunks</strong> based on a certain frequency (every <strong>minute</strong>, <strong>hour</strong>, or <strong>day</strong>).</p>

<p>For example, the period <code>[10, 10000]</code> (in <strong>seconds</strong>) would be partitioned into the following <strong>time chunks</strong> with these frequencies:</p>

<ul>
	<li>Every <strong>minute</strong> (60-second chunks): <code>[10,69]</code>, <code>[70,129]</code>, <code>[130,189]</code>, <code>...</code>, <code>[9970,10000]</code></li>
	<li>Every <strong>hour</strong> (3600-second chunks): <code>[10,3609]</code>, <code>[3610,7209]</code>, <code>[7210,10000]</code></li>
	<li>Every <strong>day</strong> (86400-second chunks): <code>[10,10000]</code></li>
</ul>

<p>Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (<code>10000</code> in the above example).</p>

<p>Design and implement an API to help the company with their analysis.</p>

<p>Implement the <code>TweetCounts</code> class:</p>

<ul>
	<li><code>TweetCounts()</code> Initializes the <code>TweetCounts</code> object.</li>
	<li><code>void recordTweet(String tweetName, int time)</code> Stores the <code>tweetName</code> at the recorded <code>time</code> (in <strong>seconds</strong>).</li>
	<li><code>List&lt;Integer&gt; getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)</code> Returns a list of integers representing the number of tweets with <code>tweetName</code> in each <strong>time chunk</strong> for the given period of time <code>[startTime, endTime]</code> (in <strong>seconds</strong>) and frequency <code>freq</code>.
	<ul>
		<li><code>freq</code> is one of <code>"minute"</code>, <code>"hour"</code>, or <code>"day"</code> representing a frequency of every <strong>minute</strong>, <strong>hour</strong>, or <strong>day</strong> respectively.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example:</strong></p>

<pre><strong>Input</strong>
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

<strong>Output</strong>
[null,null,null,null,[2],[2,1],null,[4]]

<strong>Explanation</strong>
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);                              // New tweet "tweet3" at time 0
tweetCounts.recordTweet("tweet3", 60);                             // New tweet "tweet3" at time 60
tweetCounts.recordTweet("tweet3", 10);                             // New tweet "tweet3" at time 10
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]; chunk [0,59] had 2 tweets
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
tweetCounts.recordTweet("tweet3", 120);                            // New tweet "tweet3" at time 120
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]; chunk [0,210] had 4 tweets
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= time, startTime, endTime &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= endTime - startTime &lt;= 10<sup>4</sup></code></li>
	<li>There will be at most <code>10<sup>4</sup></code> calls <strong>in total</strong> to <code>recordTweet</code> and <code>getTweetCountsPerFrequency</code>.</li>
</ul>
</div></div>
