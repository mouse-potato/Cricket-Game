# Cricket-Game

<h2>Game of Cricket Between Client and Server</h2>

<h2>Description</h2>
Each game is played for 10 balls. A toss in the beginning decides who gets to
choose to bat/bowl first. The server plays by generating a random number at
each ball and the client plays by entering a number. If both sides enter the same
number then the batting side loses a wicket. After every shot, the current scores
and wickets of the batting side are displayed along with over details. The game
can be played by multiple players if they both know the IP address of the other
player.

<h2> There are 3 files</h2>
  <ol>
    <li>single_player_server.py</li>
    <li>multi_player_server.py</li>
    <li>client.py</li>
  </ol>
  
<h2> Syntax</h2>
  <ol>
  <b><li>Single-player</b></li>
    Run single_player_server.py first then client.py (in different terminals)<br>
    python3 single_player_server.py<br>
    python3 client.py  <br>
    <b><li>Mutli-player</b></li>
    Run multi_player_server.py first then client.py (in different terminals)<br>
    python3 multi_player_server.py<br>
    python3 client.py<br>
    
<h2>Network Concepts Used</h2>
<ol>
	<li>Socket Programming</li>
</ol>

