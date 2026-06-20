---
title: "Weather"
wiki_source: "Modding:Weather data"
permalink: /Modding:Weather_data/
category: locations
tags: [weather-data, data, algorithm, forced-weather, generated-weather, tv-channel, weather-icon, rain-totem]
---
← <a href="Modding_Index" class="wikilink" title="Index">Index</a>

This page documents how the game generates
<a href="weather" class="wikilink" title="weather">weather</a> in the
game.

## Data

The weather is controlled by the string field
`Game1::weatherForTomorrow`. The possible values are:

| value       | constant             | weather    |
|-------------|----------------------|------------|
| `Sun`       | `weather_sunny`      | sunny      |
| `Rain`      | `weather_rain`       | rain       |
| `GreenRain` | `weather_green_rain` | green rain |
| `Wind`      | `weather_debris`     | windy      |
| `Storm`     | `weather_lightning`  | lightning  |
| `Festival`  | `weather_festival`   | festival   |
| `Snow`      | `weather_snow`       | snow       |
| `Wedding`   | `weather_wedding`    | wedding    |

## Algorithm

You can now change the weather algorithm by editing
<a href="Modding_Migrate_to_Stardew_Valley_1.6#Custom_location_contexts"
class="wikilink" title="location context data">location context data</a>,
and (with a C# mod) implement custom weathers.

Fields like `Game1.weather` and `Game1.weatherForTomorrow` are now
strings to support custom mod weather IDs. The change for vanilla
weather has no effect on Content Patcher packs, since the new weather
IDs match the ones Content Patcher was using before (i.e. `Sun`, `Rain`,
`Snow`, `Storm`, and `Wind`). C# mods may also see a `Festival` weather,
while Content Patcher packs will see `Sun` for it. The constants like
`Game1.weather_sunny` have the new string values (with new constants
like `Game1.legacy_weather_sunny` for the legacy values).

The base game will treat an invalid weather as sunny. C# mods can
implement custom weather effects using
<a href="Modding_Modder_Guide_APIs_Events" class="wikilink"
title="normal SMAPI events">normal SMAPI events</a> like `UpdateTicked`,
or by <a href="Modding_Modder_Guide_APIs_Harmony" class="wikilink"
title="patching">patching</a> methods like `Game1.ApplyWeatherForNewDay`
and `Game1.populateDebrisWeatherArray`.

### Forced weather

Certain dates always have the same weather:

| date              | weather             |
|-------------------|---------------------|
| spring 1          | `weather_sunny`     |
| spring 2 (year 1) | `weather_sunny`     |
| spring 3 (year 1) | `weather_rain`      |
| spring 4 (year 1) | `weather_sunny`     |
| summer 1          | `weather_sunny`     |
| summer 13         | `weather_lightning` |
| summer 26         | `weather_lightning` |
| fall 1            | `weather_sunny`     |
| winter 1          | `weather_sunny`     |

Green rain can only occur on Summer 5, 6, 7, 14, 16, 18 and 23.

Active festivals (defined in `Data/Festivals`) always have the
`Festival` weather while passive festivals (defined in
`Data/PassiveFestivals`) always have the `Sun` weather.

### Generated weather

Weather in Stardew Valley is set within the `Game1::newDayAfterFade()`
function (after the day change code, but before SMAPI's
`SaveEvents.BeforeSave` event).

The game follows these steps to decide which weather and debris to set
for the next day:

1.  Load the possible weather for the new day for each location, which
    is set just after the old day started.
2.  Check for
    <a href="#Forced_weather" class="wikilink" title="forced weather">forced
    weather</a>.
3.  If today is a wedding, set the weather to `Wedding`.
4.  Sync the `WeatherForTomorrow` field for each location.
5.  Set `Game1::wasRainingYesterday` based on whether it was raining or
    storming.
6.  Clear the debris weather array.
7.  Reset all weather flags, and sets them in the following pattern
    1.  If it is going to rain, set the rain flag to true (this does
        *not* include the green rain).
    2.  If the weather is green rain, set the green rain flag to true.
    3.  If it is going to storm, set the rain and storm flags to true.
    4.  If it is going to be windy, set the debris flag to true.
    5.  If it is going to snow, set the snow flag to true,
8.  Prepare for the possible weather the day after the new day:
    1.  Default to `Sun`;
    2.  If the day after the new day is an active festival, set the
        weather to be `Festival` and return;
    3.  If the day after the new day is a passive festival, set the
        weather to be `Sun` and return;
    4.  Apply randomized <a
        href="Modding_Migrate_to_Stardew_Valley_1.6#What&#39;s_new_for_locations_&amp;_weather#Custom_location_contexts"
        class="wikilink" title="weather conditions">weather conditions</a>
        from location contexts to get a possible weather.
9.  Prepare for the possible weather the day after the new day for those
    locations with <a
    href="Modding_Migrate_to_Stardew_Valley_1.6#What&#39;s_new_for_locations_&amp;_weather#Custom_location_contexts"
    class="wikilink"
    title="CopyWeatherFromLocation"><samp>CopyWeatherFromLocation</samp></a>
    specified (copy from source locations).
10. Sync the weather.
11. Apply all the weather flags to the valley area.
12. Populate the debris array if it is debris weather.
13. Reset (on the first day of a month) or increment the
    `monthlyNonRainyDayCount` for each location.
14. Apply the green rain response logic (*e.g.*, show global message,
    send a mail, etc.)

At this point, the main function is done setting weather.

### TV Channel

The TV will check the weather and show the following message:

<table>
<thead>
<tr>
<th><p>weather</p></th>
<th><p>message</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><samp>Festival</samp></p></td>
<td><p>"It's going to be clear and sunny tomorrow... perfect weather for
the Festival! The event will take place Location, starting between Time.
Don't be late!" Failed to fetch the data: "Um... that's odd. My
information sheet just says 'null'. This is embarrassing... "</p></td>
</tr>
<tr>
<td><p><samp>Snow</samp></p></td>
<td><p>50% chance each:</p>
<ul>
<li>"Bundle up, folks. It's going to snow tomorrow!"</li>
<li>"Expect a few inches of snow tomorrow."</li>
</ul></td>
</tr>
<tr>
<td><p><samp>Rain</samp></p></td>
<td><p>"It's going to rain all day tomorrow"</p></td>
</tr>
<tr>
<td><p><samp>GreenRain</samp></p></td>
<td><p>"Um... There appears to be some kind of... anomalous reading...
I... don't know what this means..."</p></td>
</tr>
<tr>
<td><p><samp>Storm</samp></p></td>
<td><p>"Looks like a storm is approaching. Thunder and lightning is
expected."</p></td>
</tr>
<tr>
<td><p><samp>Wind</samp></p></td>
<td><p>Per condition:</p>
<ul>
<li>Spring: "Partially cloudy with a light breeze. Expect lots of
pollen!"</li>
<li>Fall: "It's going to be cloudy, with gusts of wind throughout the
day."</li>
<li>Default: "It's going to snow all day. Make sure you bundle up,
folks!"</li>
</ul></td>
</tr>
<tr>
<td><p><em>default</em></p></td>
<td><p>50% chance each:</p>
<ul>
<li>"It's going to be clear and sunny all day."</li>
<li>"It's going to be a beautiful, sunny day tommorow!"</li>
</ul></td>
</tr>
</tbody>
</table>

**Note:** the TV will not necessarily be accurate for any other day than
non festival days, the first of the month and the 3rd of spring, which
are force-set by the `Game1::newDayAfterFade` method. Farmhands (and not
host players) may not even get that accuracy for the first of the month
and 3rd of spring.

**Note 2:** Passive festivals such as the Night Market are not
considered to have "festival" weather. Instead, all passive festivals in
the valley have "sunny" weather.

### Weather Icon

The weather icon is set in `Game1::updateWeatherIcon`, which sets an
index in `LooseSprite/Cursors.xnb`:

1.  If snowing: 7.
2.  If sunny: 2.
3.  If wedding: 0.
4.  If festival: 1.
5.  If raining: 4.
6.  If stormy: 5.
7.  If spring: debris weather is 3.
8.  If summer: unset (defaults to sunny).
9.  If fall: 6.
10. If winter: 7 (same as snowing).
11. If green rain: 999.

### Rain Totem

The rain totem (item \#681) and is controlled by `Object::rainTotem`,
which is invoked by `Object::performUseAction`. If tomorrow is a
festival day, the item is used up but nothing happens. Otherwise, it
uses up the item and sets the weather for tomorrow to `weather_rain` and
displays the message.

## Weather probability by type

This section explains the probability of each weather type. This only
applies on dates with no
<a href="#Forced_weather" class="wikilink" title="forced weather">forced
weather</a>.

### Sunny

Sunny weather covers weather variables 0, 4, and 6.

- Spring: there's an 18.3% base chance of rain (81.7% chance remaining
  for other weathers). If it doesn't rain, there's an 80% chance to
  remain sunny (except on spring 3, which will always be rainy). That
  means that in spring there's a 66.4% chance of sunny weather.
- Summer: The chance of sunny weather diminishes steadily per day from
  87.4% on summer 1 to 79.9% on summer 28. The precise chance is 1 -
  \[12% + (0.3% \* day of the month)\] per day, with a 0% chance on day
  1.
- Fall: identical to spring, but no forced weather.
- Winter: there's a 63% chance of precipitation, so only a 37% chance of
  sunny weather.

### Rainy

- Spring: there's an 18.3% base chance of rain. If it rains, there's a
  25% chance of storms *except in year 1*. So the rain odds in Spring is
  a flat 18.3% in year 1, and 13.725% in year 2 or later. It will always
  rain on spring 3 (year 1).
- Summer: the chance of rainy weather increases steadily per day from
  12.6% on summer 2 to 20.1% on Summer 27. There's an 85% chance that
  rain becomes storms. So you have a scale of \[12% + (0.3% \* day of
  the month)\] \* .15 to determine your chances of rainfall.
- Fall: same as spring, except fall in year 1 can be stormy so it's a
  flat 13.725% chance.
- Winter: never rains.

### Debris

Debris weather covers weather variable 2.

- Spring: there's a 20% chance of this after rain, so approximately
  16.6% chance of debris weather.
- Summer: no debris weather.
- Fall: there's a 60% chance for this after rain, so approximately 49.8%
  chance of debris weather.
- Winter: no debris weather.

### Stormy

Stormy weather covers weather variable 3.

- Spring: 4.57% chance of storms.
- Summer: variable chance of storms; starts at 10.71% and increases to
  17.085%.
- Fall: 4.57% chance of storms.
- Winter: no stormy weather.

### Snowy

In winter, there's a 63% chance of snow. No other season has snow.

## Save files

The save file is a snapshot of the day at 0600 the next morning. The
`WeatherForTommorow` field was used to calculate the weather, but
changing it has no effect on the weather since the weather flags have
already been set by this point. To change the weather, you need to set
one of these combinations of flags:

| weather | `isRaining` | `isDebrisWeather` | `isLightning` | `isSnowing` | `isGreenRain` |
|----|----|----|----|----|----|
| sunny | ☐ | ☐ | ☐ | ☐ | ☐ |
| rainy | ☑ | ☐ | ☐ | ☐ | ☐ |
| stormy | ☑ | ☐ | ☑ | ☐ | ☐ |
| debris | ☐ | ☑ | ☐ | ☐ | ☐ |
| snowy | ☐ | ☐ | ☐ | ☑ | ☐ |
| festival | ☐ | ☐ | ☐ | ☐ | ☐ |
| wedding | ☐ | ☐ | ☐ | ☐ | ☐ |
| green rain | ☐ | ☐ | ☐ | ☐ | ☑ |

**Note:** changing `isDebrisWeather` during an active game will not
create the array. You'll need to call
`Game1::populateDebrisWeatherArray` to get the debris populated.
Correspondingly, if you're removing the debris weather flag, remember to
call `Game1::debrisWeather::Clear`.

## Notes/FAQ

- The TV can be fixed by overriding it - or just by using Entoroax's
  Framework.
- You can set snow and debris at any time, the game just won't.
- You cannot set debris and rain at the same time.

<a href="Category_Modding" class="wikilink"
title="Category:Modding">Category:Modding</a>

<a href="pt_Modificações_Dados_climáticos" class="wikilink"
title="pt:Modificações:Dados climáticos">pt:Modificações:Dados
climáticos</a>
<a href="ru_Модификации_Погодные_явления" class="wikilink"
title="ru:Модификации:Погодные явления">ru:Модификации:Погодные
явления</a> <a href="zh_模组_天气数据" class="wikilink"
title="zh:模组:天气数据">zh:模组:天气数据</a>
