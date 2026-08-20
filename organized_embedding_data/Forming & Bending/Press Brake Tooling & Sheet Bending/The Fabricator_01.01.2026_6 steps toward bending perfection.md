# 6 steps toward bending perfection

[TARİH: 01.01.2026 The Fabricator]

Cover Story

How to make forming as error-free as possible

By

Tim Heston

Images: Cincinnati Incorporated

T

he press brake department has been called the heart of precision sheet metal fabrication. What happens there affects what happens upstream in cutting and downstream in welding and beyond.

How can you create smooth, predictable job flow in the forming department? To find out, The Fabricator spoke with Mike Crossland, bending product manager, and Edwin Diaz, software product manager, at Cincinnati Incorporated about six basic steps you can take to minimize errors in the forming department. They clarified that the list doesn’t cover every scenario, of course, but overall, it still provides a solid foundation for future improvement.

1. USE THE CORRECT V-DIE WIDTH

"The biggest errors we see tend to be about tool selection," Crossland said. "And typically, the lower V die is off. The die opening determines your inside bend radius, which in turn determines your blank size. So, when you use the wrong V die width or angle, you throw off your flange dimensions."

A review of the basics here can help. When you bend sheet metal, the piece elongates at the outside radius. The

k-factor

, which describes the extent of that elongation, is incorporated into the

bend allowance

equation, which gives you the distance around the radius after elongation (or stretching) from forming. You use the

bend deduction

to subtract (or deduct) the material you need to accommodate for that stretching. This gives you a slightly smaller blank size that, when formed, grows to the overall dimension you need. Buried within that bend allowance calculation is the inside radius.

The bending method matters here. Modern press brakes air-bend almost exclusively. During air bending, the punch’s depth of penetration into the die space determines the bend angle (see

Figure 1

). And for most mild steels, stainless steels, and harder (tempered) aluminums, the inside radius forms as a percentage of the die width. Change the die width, and you change your radius. When forming materials like soft aluminums, the punch nose can determine the air-formed radius. Regardless, bend calculations need to incorporate the

actual

radius the shop’s press brake tools create.

2. USE THE CORRECT DIE ANGLE

Although the process doesn’t dominate the industry like it once did, bottoming still has its place. "Bottoming is actually very beneficial when a very small inside bend radius is called out," Crossland said.

Die angles in bottom bending matter a great deal, of course. As the punch descends, the material wraps around the punch body; then, as the ram continues to apply tonnage, the sheet metal "bottoms" against the die angle. So, the die angle (plus a small amount for springback) sets the bend angle, and the punch tip defines the inside bend radius, which can be smaller than a comparable air bending process. (A disadvantage of bottoming: You can’t adjust for springback without changing your die angle.)

FIGURE 1

This conventional air bending setup shows how the punch’s depth of penetration into the die space determines the bend angle. The radius forms as a percentage of the die width. The bending method has three points of contact: at the punch tip and the two die shoulders. Note the die angle, which is much narrower than the 90-degree bend being formed.

But what about air bending? The punch descends to a specific point; the moment it releases pressure and reverses, the metal springs back to the desired angle. If the angle is slightly underbent, the operator increases the depth of penetration slightly to dial in the setup. In all this, the outside material surface touches the die

only

on the two die shoulders. Considering this, why would the die angle matter?

"All the air bend formulas work until the moment the material starts touching the bottom of the V in the die," Crossland said. "For most air bending applications, you need to use dies that are 70 degrees and less."

The narrower die angle creates a deeper die space and gives the clearance you need to overbend and account for springback. If you use an angle that’s too wide and shallow, your depth of penetration reaches the bottom of the V. In an air bend, when the material’s outside bend radius touches the bottom of the V, the entire nature of the bend changes and, practically speaking, becomes unpredictable.

When the material’s outside bend radius first makes contact with the bottom of the V, the legs of the bend move and eventually lift off the die shoulders. The radius changes even further if the ram continues to apply pressure and forces the material to wrap around the punch body (see

Figure 2

). At this point, the bend no longer has three points of contact (punch tip plus the two die shoulders), which means the air bending formulas fall apart.

3. DIAL IN YOUR DIE WIDTH FOR BUMP BENDS

Bump bending, sometimes called step or incremental bending, is notorious for being difficult to predict. But it doesn’t have to be, especially if material properties, including thickness and tensile strength, are consistent.

FIGURE 2

This shows an air bend gone awry—and why die angles matter. It’s an exaggerated illustration of what happens when the punch tip hits the bottom of the V in an air bend. The part no longer touches the lead-in shoulder radii of the V, essentially changing the V opening.

FIGURE 3

This bump bend has varying pitches, or distances between the bumped bend lines. Tool selection needs to account for this. The narrower the pitch, the narrower the die opening you need.

The trick is ensuring every bump is formed with just three points of contact—the two die shoulders and the punch tip. Most critically, a previously "bumped" bend should never be in the die space. As Diaz explained, that’s a telltale sign that the die opening is too wide for the job. As long as tonnage issues don’t arise, the smaller the die opening you use, the smaller the pitch (space between bumps) can be, and the smoother the final bend (see

Figure 3

).

Diaz added that bump bends with inconsistent pitches require special scrutiny. "I actually worked with a part recently where I saw 11 different bumps, but all of them were spaced unevenly." It turned out that the chosen die width was too wide for nearly half of those bumps. This threw off the calculations for the entire step bend.

Today, offline bend software can calculate incremental bends accurately, as long as the tooling is correct. The software looks at each bump as a kind of mini air bend, one with a very open angle, wide radius, and two straight legs that rest on the die shoulders—again, just three points of contact. If the operator chooses different tooling, and one of those legs suspended over the die space has a bend from a previous bump, the bend calculations fail.

Bump bends produce visible bend lines that might not be acceptable, which is why some large-radius bends are produced with special toolsets. Crossland described one setup in which a round punch descends several times into a urethane die—a tool that works wonders for creating cosmetically critical forms. But if productivity is the issue, not cosmetics, he explained that you might want to think twice before moving to a urethane pad, especially for low-volume parts. Yes, the setup takes just one or a few hits, but predicting how the bend will behave isn’t easy.

"When you bump-bend the conventional way, over a narrow V, you can save the steps, and once you have it dialed in, it’s very repeatable," Crossland said. "Using urethane really becomes an art form, with a lot of trial and error. And once you save the setup, you still need to adjust for urethane wear when the job runs again later."

4. WHEN AIR BENDING, UNDERBEND, THEN CORRECT

An underbent part is just incomplete, as long as the final adjustment and rehit is accurate; an overbent part is usually scrap. Sure, a part program written specifically for one press brake that’s fed consistent material might be able to form the first part complete, without underbending and adjusting. But as sources explained, most new part programs that use air bending, whether programmed at the machine or offline, are written to produce slightly underbent parts.

FIGURE 4

Indicator lights on the press brake cylinder cover show the current state of a machine.

"This is on purpose," Crossland said. "This accounts for variations in material, tooling, and different machines."

Every material has thickness and tensile strength tolerances that require press brakes to adapt, especially if those tolerances are very tight. Underbending should occur by default when the press brake operates in a mode designed for air bending; some machine controllers call this

angle mode

. Because the machine knows the location of the punch tip, surface of the V die, and the die width, it knows exactly how far the punch should descend—close enough to make the final adjustments easy, but not so close as to risk overbending the piece.

Press brake modes that dial in the exact ram position at the bottom of the stroke—sometimes called

position mode

or

absolute mode

— work well when bottoming or when using specialty tools with unique ram positioning requirements. If you use these modes for conventional air bending and you are producing a lot of overbent scrap, you might want to return to the mode that was designed for the air bending process.

These days, the practice of underbending can be automated if a brake has automatic angle detection. The technology can help make "first part, good part" a reality. If you rehit an underbent part manually, you might find it difficult to realign the bend line exactly, especially if it’s a large-radius bend. And even if the bend line is marked, you need to keep your hands steady before the tool makes contact.

Good communication, training, and software keep everyone on the same page. Every operator should know what an efficient, accurate bending operation requires.

"The [manual] rehit is by feel," Crossland said, "but when you rely on automatic angle measuring, the machine never lets go of the part."

Pressure sensors or cameras can detect the bend, after which the system adjusts to dial in the bend angle. The process does add a bit of cycle time, so performing it on every part might be overkill. Many operations make use of angle detection to bend the first part, then turn it off for the remaining parts in a batch.

5. COMMUNICATE, PERSONALLY AND DIGITALLY

You’ve instituted training regimens and process documentation. You have no "pedal pushers" who bend parts with little knowledge of what’s going on in front of them. And you use offline programming that simulates forming jobs based on the tools operators actually use.

"The software adjusts the forming program based on available tooling," Diaz said, "then communicates with nesting so it can adjust the blank size to accommodate."

With this foundation set, you might have meetings with forming department supervisors and managers:

The offline bend program uses tools and a bend sequence that one of our experienced operators doesn’t like. Can he change it, and if so, what should the guardrails be?

As Crossland explained, the answer will depend on the fabricator. You might have certain guardrails to keep operational consistency. For instance, you probably don’t want one operator air bending with a 70-degree die and another bottoming with a 90-degree die for the same part.

Diaz added that any change made should be documented fully. Changes shouldn’t affect the part’s design or integrity, or make life difficult for those up and downstream. In such scenarios, offline bend programming can really shine.

"You can set different rules in the software so the system always looks for a bend sequence that represents the fastest route to a formed part," Diaz said. "This includes flips and rotations. It’s like your car’s navigation system. It shows five different routes to your destination, and it gives you what it calculates to be the fastest route."

Even so, some operators might have an easier time with different bend sequence "routes." For instance, one operator might have an easier time holding a large blank steadily against the backgauge with the long flange behind the tools; another operator might prefer gauging against the short flange.

Here, talking with operators about preferred tools and bend sequences can help. In fact, such communication can be critical when implementing offline bending software. "When there’s no communication between engineering and your operators, you can run into challenges," Diaz said. "Operators should go to the office, and engineers should go to the floor. An experienced operator could also be your offline programmer. In fact, that’s often ideal."

The simulation carries over to the press brake control, where clear graphics can help error-proof a job. For instance, the control can color-code certain flanges to signify which are up-bends and which are down-bends, so you avoid bending parts backward.

6. MONITOR AND IMPROVE

A bending department with operators who know the fundamentals, follow documented procedures, and communicate regularly can be incredibly effective. Still, in a high-product-mix environment, inefficiencies can get lost in the shuffle.

Sources pointed to several tools that could help. First is visual management. Some brakes today have lights on them that show different states: green for producing, yellow for setup, and red for down and unavailable (see

Figure 4

).

These can complement production monitoring software that tracks the time a press brake ram

actually moves

, versus the time the machine spends idle or in setup. "Every little thing counts, and there’s a lot of data running in the backround, including stroke counts and other productivity measures," Diaz said. "You’ve made investments in your equipment, and you should see what they’re doing and how they’re performing."

For instance, an operator might clock in on the job with the ERP, spend time with a challenging setup, then finally bending the job before clocking out. For months, that challenging setup goes unnoticed; people just assume the job cycle time is what it is.

But when monitoring software shines a light on the issue, problem-solving commences. The forming team might find a way to make the setup less challenging, or it might not. Regardless, process monitoring at least prevents the issue from remaining hidden.

Good communication, training, and software keep everyone on the same page. Every operator knows what an efficient, accurate bending operation requires. Each might have a favorite route (like a preferred bend sequence), but they’re all reading from the same roadmap—always working to minimize errors and continually improve.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

Cincinnati Incorporated,

www.e-ci.com