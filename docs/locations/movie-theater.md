---
title: "Movie Theater"
wiki_source: "Modding:Movie theater data"
permalink: /Modding:Movie_theater_data/
category: locations
tags: [movie-theater-data, movie-data, format, movie-reactions, movie-identifiers, concession-data, concession-tastes, concession-tags]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page explains how the files associated with the
<a href="Movie_Theater" class="wikilink" title="Movie Theater">Movie
Theater</a>, what each of them do, and how they are formatted. This is
an advanced guide for mod developers.

## Movie data

`Data\Movies.xnb` contains the data for all movies, including their
names, descriptions, genre tags, scenes, and dialogue and narration
spoken within the film. For reference, below is the raw data of "The
Brave Little Sapling" as of :

### Format

The `Data/Movies` asset is a list of models, which have the following
fields:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Id</samp></p></td>
<td><p>A <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> which
identifies this movie. This should only contain
alphanumeric/underscore/dot characters.</p></td>
</tr>
<tr>
<td><p><samp>Seasons</samp></p></td>
<td><p><em>(Optional)</em> The seasons when the movie should play, or
omit for any season. For example:</p>
<div class="sourceCode" id="cb1"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;Seasons&quot;</span><span class="er">:</span> <span class="ot">[</span> <span class="st">&quot;Spring&quot;</span><span class="ot">,</span> <span class="st">&quot;Summer&quot;</span> <span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>YearModulus</samp><br />
<samp>YearRemainder</samp></p></td>
<td><p><em>(Optional)</em> If set, plays the movie on alternating years
based on the formula <samp>theater_age % modulus == remainder</samp>,
where <samp>theater_age</samp> is the number of years since the movie
theater was built. If omitted, the movie plays in any year.</p>
<p>For example:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="er">//</span> <span class="er">play</span> <span class="er">in</span> <span class="er">the</span> <span class="er">first</span> <span class="er">year,</span> <span class="er">and</span> <span class="er">every</span> <span class="er">second</span> <span class="er">year</span> <span class="er">thereafter</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;YearModulus&quot;</span><span class="er">:</span> <span class="dv">2</span><span class="er">,</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;YearRemainder&quot;</span><span class="er">:</span> <span class="dv">0</span></span></code></pre></div>
<div class="sourceCode" id="cb3"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="er">//</span> <span class="er">play</span> <span class="er">in</span> <span class="er">the</span> <span class="er">second</span> <span class="er">year,</span> <span class="er">and</span> <span class="er">every</span> <span class="er">second</span> <span class="er">year</span> <span class="er">thereafter</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;YearModulus&quot;</span><span class="er">:</span> <span class="dv">2</span><span class="er">,</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;YearRemainder&quot;</span><span class="er">:</span> <span class="dv">1</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Texture</samp></p></td>
<td><p><em>(Optional)</em> The asset name for the movie poster and
screen images, or omit to use <samp>LooseSprites\Movies</samp>.</p>
<p>This must be a spritesheet with one 490×128 pixel row per movie. A
13×19 area in the top-left corner of the row should contain the movie
poster. With a 16-pixel offset from the left edge, there should be two
rows of five 90×61 pixel movie screen images, with a six-pixel gap
between each image. (The movie doesn't need to use all of the image
slots.)</p></td>
</tr>
<tr>
<td><p><samp>SheetIndex</samp></p></td>
<td><p>Determines where the game looks for the movie's scene sprites
within <samp>LooseSprites\Movies.xnb</samp>. This includes the movie
poster and screen images for the movie.</p></td>
</tr>
<tr>
<td><p><samp>Title</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the title of the
film.</p></td>
</tr>
<tr>
<td><p><samp>Description</samp></p></td>
<td><p>A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the description of
the film, seen when interacting with its poster outside of the
theater.</p></td>
</tr>
<tr>
<td><p><samp>Tags</samp></p></td>
<td><p>A list of genres that apply to the movie, used to calculate an
NPC's reaction to a movie. Can be any arbitrary string; the ones
currently used in the game are: <samp>family</samp>,
<samp>comedy</samp>, <samp>horror</samp>, <samp>art</samp>,
<samp>action</samp>, <samp>sci-fi</samp>, <samp>classic</samp>,
<samp>romance</samp>, and <samp>documentary</samp>.</p></td>
</tr>
<tr>
<td><p><samp>CranePrizes</samp></p></td>
<td><p><em>(Optional)</em> The items to add to the <a
href="Movie_Theater#Crane_Game" class="wikilink"
title="crane game">crane game</a> prize pool on days when this movie is
playing, if any.</p>
<p>This consists of a list of models with these fields:</p>
<table>
<thead>
<tr>
<th><p>field</p></th>
<th><p>effect</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><em>common fields</em></p></td>
<td><p>See <a href="Modding_Item_queries#Item_spawn_fields"
class="wikilink" title="item spawn fields">item spawn fields</a> for the
generic item fields supported for crane game items.</p>
<p>If set to an <a href="Modding_Item_queries" class="wikilink"
title="item query">item query</a> which returns multiple items, one of
them will be selected at random.</p></td>
</tr>
<tr>
<td><p><samp>Rarity</samp></p></td>
<td><p><em>(Optional)</em> The prize pool to add the item to. The
possible values are <samp>1</samp> (common), <samp>2</samp> (rare), and
<samp>3</samp> (deluxe). Default <samp>1</samp>.</p></td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td><p><samp>ClearDefaultCranePrizeGroups</samp></p></td>
<td><p><em>(Optional)</em> The prize pools whose default items to
discard, so only those specified by <samp>CranePrizes</samp> are
available. Default none.</p>
<p>For example:</p>
<div class="sourceCode" id="cb4"><pre
class="sourceCode json"><code class="sourceCode json"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="st">&quot;ClearDefaultCranePrizeGroups&quot;</span><span class="er">:</span> <span class="ot">[</span> <span class="dv">2</span><span class="ot">,</span> <span class="dv">3</span> <span class="ot">]</span></span></code></pre></div></td>
</tr>
<tr>
<td><p><samp>Scenes</samp></p></td>
<td><p>A list of data blocks for the film's scenes. (See
below.)</p></td>
</tr>
</tbody>
</table>

#### Scenes

The `Scenes` is a list of blocks, each corresponding to a specific scene
in the movie. The blocks are listed in chronological order, and the data
of each one is as follows:

| key format | description |
|----|----|
| `Image` | Which image to show within the sequence of the movie's sprites in `LooseSprites\Movies.xnb`. |
| `Music` | The music track to play during the scene. Can be left blank. |
| `Sound` | The sound effect to play during the scene. Can be left blank. |
| `MessageDelay` | How long to hold the scene before displaying any text. |
| `Script` | Used for special visual/auditory effects. Written in the same format as <a href="Modding_Event_data#Event_scripts" class="wikilink"
title="event scripts">event scripts</a>. Supports <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable strings">tokenizable strings</a>. |
| `Text` | The dialogue/narration of the scene. Supports <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable strings">tokenizable strings</a>. |
| `Shake` | A boolean value which, if true, adds screen-shake. |
| `ResponsePoint` | If specified, an NPC's reaction data can reference the scene by this name in order to have a specific, timed reaction to it. |
| `ID` | An ID for the scene in the format of `<season><number>_<index>`. \<season\> and \<number\> are identical to those values in the ID of the movie itself. \<index\> is, counting from 0, what number scene this is in the movie. |

For example, this content pack adds a new 'Pufferchick II' movie which
plays in winter every third year:

## Movie reactions

`Data\MoviesReactions.xnb` contains every NPC's taste in movies and
their dialogue in response to them. For reference, below is the raw data
for <a href="Penny" class="wikilink" title="Penny">Penny</a>'s reactions
as of :

### Format

Each block of data within the file begins with an `NPCName` key, which
is the name of the NPC to whom the rest of the data in the block will
apply. This is followed by a list with the key `Reactions`. Each block
within this list is the data for an NPC's response to a specific type of
movie.

The data within each block is formatted as follows:

<table>
<thead>
<tr>
<th><p>key format</p></th>
<th><p>description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Tag</samp></p></td>
<td><p>Which category of movie this response is for. In decreasing order
of specificity, this can be:</p>
<ul>
<li><samp>*</samp>, in which case the response will always be
applicable, unless there are other restrictions applied by
<samp>Whitelist</samp></li>
<li>a genre of movie, as listed in the <samp>Tags</samp> field of a
film's data</li>
<li>the NPC's reaction to a movie, one of <samp>love</samp>,
<samp>like</samp>, or <samp>dislike</samp>.</li>
<li>a specific movie's identifier, as listed at the header of its block.
(i.e. <samp>spring_movie_0</samp> for "The Brave Little Sapling")</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Response</samp></p></td>
<td><p>One of <samp>love</samp>, <samp>like</samp>,
<samp>dislike</samp>, or <samp>reject</samp>. Used to calculate
Friendship points gained with the NPC. A loved movie earns 200
Friendship points with the NPC, a liked movie earns 100 Friendship
points, and a disliked movie neither earns nor costs friendship points
with the NPC. Rejected movies will turn down the ticket and say their
line for <a href="Modding_Dialogue#Item_dialogue" class="wikilink"
title="RejectMovieTicket_DontWantToSeeThatMovie">RejectMovieTicket_DontWantToSeeThatMovie</a>.</p></td>
</tr>
<tr>
<td><p><samp>Whitelist</samp></p></td>
<td><p>A list of NPC names. If not empty, the response will only be
applicable if, in addition to the movie matching <samp>Tag</samp>, one
of the listed NPCs is also present within the theater. Currently only
used for Penny, who has a special reaction to watching a movie if her
mother <a href="Pam" class="wikilink" title="Pam">Pam</a> is
present.</p></td>
</tr>
<tr>
<td><p><samp>SpecialResponses</samp></p></td>
<td><p>Contains the dialogue spoken by an NPC during the film in a
series of blocks. (See below.) Can be left null.</p></td>
</tr>
<tr>
<td><p><samp>ID</samp></p></td>
<td><p>A unique identifier in the form of
<samp>reaction_&lt;index&gt;</samp>, where &lt;index&gt; is, counting
from 0, what number block this is within the <samp>Reactions</samp>
list.</p></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>

For unknown reasons, in the vanilla game code, when the `Tag` field is
`love` or `dislike`, the `Response`field will always be `like`.

#### Special responses

Each `SpecialResponses` block contains 3 blocks, beginning with
`BeforeMovie`, `DuringMovie`, and `AfterMovie`, in that order. Any of
these blocks may be left null. By default, the dialogue within these
blocks triggers when talking to the NPC in the movie theater lobby, at a
random point during the movie, and after the movie is finished,
respectively. The data within each block is as follows:

| key format | description |
|----|----|
| `ResponsePoint` | If not null, this dialogue will trigger at the given response point instead of its regular timing. See the <a href="Modding_Movie_theater_data#Scenes" class="wikilink"
title="scenes field documentation">scenes field documentation</a> for an explanation of response points. |
| `Script` | A script which runs prior to `Text` being displayed. Written in the same format as <a href="Modding_Event_data#Event_scripts" class="wikilink"
title="event scripts">event scripts</a>. |
| `Text` | The dialogue spoken by the NPC. Supports <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable strings">tokenizable strings</a>. |

If multiple response blocks are applicable to the movie, the game uses
the first non-null `Response`, `BeforeMovie`, `DuringMovie`, and
`AfterMovie` fields it can find. Said data does not necessarily have to
come from the same response block. If the game cannot find applicable
`DuringMovie` dialogue, it will use default text from
`Strings\Characters.xnb`. If the game cannot find applicable
`BeforeMovie` or `AfterMovie` dialogue, the NPC will show as being able
to be spoken to, but interacting with them will have no effect.

### Movie Identifiers

| key | movie title |
|----|----|
| spring_movie_0 | <a href="Movie_Theater#Movies" class="wikilink"
title="The Brave Little Sapling">The Brave Little Sapling</a> |
| summer_movie_0 | <a href="Movie_Theater#Movies" class="wikilink"
title="Journey Of The Prairie King: The Motion Picture">Journey Of The
Prairie King: The Motion Picture</a> |
| fall_movie_0 | <a href="Movie_Theater#Movies" class="wikilink"
title="Mysterium">Mysterium</a> |
| winter_movie_0 | <a href="Movie_Theater#Movies" class="wikilink"
title="The Miracle At Coldstar Ranch">The Miracle At Coldstar Ranch</a> |
| spring_movie_1 | <a href="Movie_Theater#Movies" class="wikilink"
title="Natural Wonders: Exploring Our Vibrant World">Natural Wonders:
Exploring Our Vibrant World</a> |
| summer_movie_1 | <a href="Movie_Theater#Movies" class="wikilink"
title="Wumbus">Wumbus</a> |
| fall_movie_1 | <a href="Movie_Theater#Movies" class="wikilink"
title="It Howls In The Rain">It Howls In The Rain</a> |
| winter_movie_1 | <a href="Movie_Theater#Movies" class="wikilink"
title="The Zuzu City Express">The Zuzu City Express</a> |

## Concession data

`Data\Concessions.xnb` contains the data for the food purchased at the
concessions stand, stored as a list of blocks. For reference, below is
the raw data of the file as of :

### Format

Each block within the list corresponds to a single concession. The data
for each block is as follows:

| key format | description |
|----|----|
| `ID` | A <a href="Modding_Common_data_field_types#Unique_string_ID"
class="wikilink" title="unique string ID">unique string ID</a> to identify this entry. |
| `Name` | The internal name of the concession. |
| `DisplayName` | A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the name of the concession, which is displayed to the player in-game. |
| `Description` | A <a href="Modding_Tokenizable_strings" class="wikilink"
title="tokenizable string">tokenizable string</a> for the description of the concession. |
| `Price` | The price of the concession in . |
| `ItemTags` | A list of tags which describe the concession, used to determine an NPC's reaction to it. Can be any arbitrary string; the ones currently used in the game are: `Sweet`, `Candy`, `Drink`, `Hot`, `Healthy`, `Cold`, `Joja`, `Sour`, `Fatty`, `Salty`, `Sandwich`, `Burger`, and `Gourmet`. |
| `Texture` | The asset name for the texture containing the concession's sprite. |
| `SpriteIndex` | The index within the `Texture` for the concession sprite, where 0 is the top-left sprite. |

For example, this content pack adds a new 'Pufferchick Pop' concession
with a custom image:

## Concession tastes

`Data\ConcessionTastes.xnb` contains the data that determines an NPC's
opinion of a concession. For reference, below is the raw data of the
file:

### Format

Each block within the list has the following data:

| key format | description |
|----|----|
| `Name` | Who this block should apply to. Can be the name of an NPC or `*`, in which case the tastes will apply to every NPC. |
| `LovedTags`</br>`LikedTags`</br>`DislikedTags` | A list of concession tags that are loved, liked, or disliked. This can be an `ItemTag`, or the internal name of a specific concession. To determine an NPC's opinion of a concession, the game totals how many tags from each group apply, with `LovedTags` and `LikedTags` contributing a positive score and `DislikedTags` contributing a negative. Purchasing a loved snack earns 50 Friendship points with the NPC, a liked snack earns 25 Friendship points, and a disliked snack neither earns nor costs friendship points with the NPC. |

### Concession tags

Black Licorice is the only item that doesn't have specific concession
tags attached to it. Stardrop Sorbet is a universally loved item,
whereas Black Licorice, Joja Cola, and JojaCorn are universally disliked
items.

<table>
<thead>
<tr>
<th><p>tag</p></th>
<th><p>applicable concessions</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Burger</samp></p></td>
<td><p>Salmon Burger</p></td>
</tr>
<tr>
<td><p><samp>Candy</samp></p></td>
<td><p>Cotton Candy<br />
Jawbreaker<br />
Rock Candy<br />
Sour Slimes</p></td>
</tr>
<tr>
<td><p><samp>Cold</samp></p></td>
<td><p>Ice Cream Sandwich<br />
Joja Cola</p></td>
</tr>
<tr>
<td><p><samp>Drink</samp></p></td>
<td><p>Jasmine Tea<br />
Joja Cola<br />
Kale Smoothie</p></td>
</tr>
<tr>
<td><p><samp>Fatty</samp></p></td>
<td><p>Fries<br />
Nachos<br />
Personal Pizza</p></td>
</tr>
<tr>
<td><p><samp>Gourmet</samp></p></td>
<td><p>Cappuccino Mousse Cake<br />
Panzanella Salad<br />
Stardrop Sorbet<br />
Truffle Popcorn</p></td>
</tr>
<tr>
<td><p><samp>Healthy</samp></p></td>
<td><p>Apple Slices<br />
Hummus Snack pack<br />
Jasmine Tea<br />
Kale Smoothie<br />
Panzanella Salad</p></td>
</tr>
<tr>
<td><p><samp>Hot</samp></p></td>
<td><p>Chocolate Popcorn<br />
Fries<br />
Jasmine Tea<br />
Nachos<br />
Personal Pizza<br />
Popcorn</p></td>
</tr>
<tr>
<td><p><samp>Joja</samp></p></td>
<td><p>Joja Cola<br />
JojaCorn</p></td>
</tr>
<tr>
<td><p><samp>Salty</samp></p></td>
<td><p>Fries<br />
Nachos<br />
Popcorn<br />
Salted Peanuts<br />
Truffle Popcorn</p></td>
</tr>
<tr>
<td><p><samp>Sandwich</samp></p></td>
<td><p>Ice Cream Sandwich<br />
Salmon Burger</p></td>
</tr>
<tr>
<td><p><samp>Sour</samp></p></td>
<td><p>Sour Slimes</p></td>
</tr>
<tr>
<td><p><samp>Sweet</samp></p></td>
<td><p>Apple Slices<br />
Cappuccino Mousse Cake<br />
Chocolate Popcorn<br />
Cotton Candy<br />
Ice Cream Sandwich<br />
Jawbreaker<br />
Rock Candy<br />
Star Cookie<br />
Stardrop Sorbet</p></td>
</tr>
</tbody>
</table>

## Movie selection

Since the `Data/Movies` asset is a list, its order determines the order
movies are shown within a season. If multiple movies can play in the
same season, each movie will be shown for an equal block of days within
the month (e.g. four movies will each play for seven consecutive days).
If there are more movies than days, 28 movies will be chosen at random
to play that month.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="ru_Модификации_Кинотеатр" class="wikilink"
title="ru:Модификации:Кинотеатр">ru:Модификации:Кинотеатр</a>
<a href="zh_模组_电影院数据" class="wikilink"
title="zh:模组:电影院数据">zh:模组:电影院数据</a>
