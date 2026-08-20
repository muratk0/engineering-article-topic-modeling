# A holistic look at nesting

[TARİH: 01.10.2025 The Fabricator]

Tech Spotlight

Streamline the quote-to-cut process

By

Tim Heston

NIKITA ARMYAGOV/iStock/Getty Images Plus

W

hen people think of nesting for laser cutting (or other thermal cutting processes), they think of putting together a puzzle that maximizes material yield, minimizes waste, and ensures a reliable process—no tip-ups; minimal distortion; just constant, predictable cutting.

But this is just a portion of the picture, especially for sheet metal and plate job shops that bid on orders continually. One of the greatest inefficiencies within the job shop is the "guesstimation" that goes on in quoting, especially with homegrown spreadsheets. The process usually doesn’t involve precise nesting. Also, the customer-provided drawing estimators rely on provides an incomplete picture that doesn’t account for the host of order processing activities. A shop might send an accepted order through the engineering department, but in truth, they’re not engineering anything. They’re just cleaning up messy files.

"That’s the mission behind automating the file cleanup, especially when you need to reply quickly with a quote, and you don’t have time to find all the errors and fix them."

That was Geoff Prince, vice president of Irvine, Calif.-based PEP Technology. The company offers a nesting platform that, through a tool called the CAD Converter, aims to automate the cleanup and, ultimately, streamline what happens between the initial quote and the first cut.

From PDF to CAD to Cut

Many fabricators talk about the challenge of customers sending PDFs with a request-forquote (RFQ) package—especially raster PDFs, which are essentially pixelated representations.

"We now have tools to allow users to get a usable drawing from those most of the time. It depends on the quality. If you have a raster-based PDF that’s a scan from a previously faxed document, that of course will be difficult. But if it’s a vector-based PDF, eight times out 10 you can get a quality conversion."

That was Justin Heiland, application engineer at PEP, adding that converting the PDF is just one part of a larger process ripe for automation.

"Because we’re working with a picture, every arc in the drawing is really a line segment. But now, we have tools that understand the deviations and initiate replacement routines."

This includes text that, again, in a PDF, is a series of lines or pixels. "We now can turn this into text we can read, so we can scale the entire drawing to make sure these dimensions are all correct and within tolerance. Now that you’ve created the drawing, I can convert it [using CAD Converter] and quickly attach this to a quote for a customer."

Heiland added that automated PDF conversion—a feature offered within CAD Converter—often works best in specific scenarios. These include quick-turn bids as well as in applications where getting a DXF, STEP, or other drawing file just isn’t possible.

"The first shop that returns an accurate quote often will win the job," Heiland said, adding that this fact often reveals a common challenge: quick response wins the order, but accuracy almost always suffers. "Estimators who receive PDFs often just give a ballpark estimate off a gross area, and they just hope it’s close enough.

Sometimes they send an email to customers to request a DXF." Unfortunately, customers don’t always respond with a DXF quickly. Besides, it adds friction to the customer experience. Customers want a price, and they want it quickly.

The PDF tool helps remove that friction while not submitting rough "guesstimate" bids. "Estimators’ first email to the customer won’t be, ‘Can you send a DXF?’ It can instead be, ‘Here’s your quote.’"

Again, PDF conversion isn’t perfect, especially if the source material is poor. So, once the job is won, it often makes sense to ask the customer for a drawing file, if one is available. Before a job is won, however, every minute that goes by can make the difference between winning and losing an order.

The Importance of File Cleanup

Sources emphasized that PDF file conversion alone really doesn’t solve the industry’s principal problem: the time highly qualified people spend tediously clicking through drawing files. All this time is one reason why most shop quotes are based on guesses, not reality—even if customers supply complete drawing files.

Shop estimating departments often make a hard choice: Do they return a rough quote, potentially losing money on a job, or do they spend precious time cleaning up the file—and risk losing the work entirely? Understandably, many rely on homegrown spreadsheets and choose quoting speed over accuracy. After all, the industry average bid-win rates hover around 30%, according to the latest KPI surveys from the Fabricators and Manufacturers Association. Why spend time cleaning up files that likely will never be cut?

"Traditionally, estimators use spreadsheets that incorporate linear inches around a part exterior," Prince said, "and they’ll base the number of pierces off that. They’ll then use a feed rate based on the material thickness." This overlooks all the moves a cutting head needs to make for those interior cutouts. "And unless they have a clean file, they’re not going to nest the part at all. So, they quote based off the rectangular area of the part. This ignores how parts can interlock and be arranged [to save space on the sheet], and it usually means they include more material in that quote than they need."

This, sources said, explains the importance of automating the file cleanup and nesting at the quoting stage. When an RFQ comes in the door, the CAD Converter cleans up files automatically. It identifies multiple parts within a job packet, corrects the splines, detects minute gaps, identifies dimension callouts to ensure proper scaling, and highlights certain edges parallel to bend lines, noting that they’ll need to be flush against a press brake’s backgauge (and so, ideally, should not have a microjoint tab).

Drawing file cleanup before nesting—including catching splines and closing gaps in the part profile—can consume much of the CAD technician’s day in the office. Also, one wrong click can snowball into larger problems downstream.

PEP Technology

The clean part drawings then are sent to the nesting engine that now can place them within a sheet and identify the true material usage. All this automation helps create an accurate quote quickly. Estimators aren’t guessing, but they’re also not spending hours redrawing and cleaning up files on a job that might never be won.

Once the order is won, next steps can depend on the job and best practices at a particular shop. They could run with the file they have, or (especially if the original bid packet only had PDFs) they could ask the customer for the latest drawing files, just to have the most up-to-date and complete source files possible, at which point they would be sent through automated file cleanup again.

Here, operations with precision forming might send files through a bend simulator (like PEP Bend), which accounts for elongation created by the actual punches and V dies being used on the floor—so the blanks are sized just right.

From here, the nesting engine identifies lead-in and lead-outs and potential areas for common-line cutting, as well as strategies to minimize excess heat and the potential distortion. Parts for one job might be cut on a single sheet or spread among many sheets. The grid can be made visible to ensure parts lay across the slats when possible, to minimize the need for microtabbing and prolong slat life. This also helps identify slugs susceptible for tip-ups, and the potential for slug- and skeleton-destruct sequences. Certain microtab designs promote breakaway into the part itself, instead of into the skeleton web—eliminating secondary deburring. So, instead of a burr, the part edge has an ever-so-minute divot—a strategy that can work for edges that will be hidden or welded.

Avoid the Inefficiency Snowball

Automated nesting has evolved significantly in recent years. It’s become more than just finding the best material utilization or even the most reliable toolpaths. It’s also about automating the processes that happen before the final nest is developed.

To illustrate, Heiland described the issue of missed splines around curves. "When this happens, you basically send a part with a bunch of tiny line segments to the laser." If not corrected (that is, replaced with a simple arc), splines can wreak havoc on laser cutting quality, with scalloped edges and a telltale "stuttering" of the laser head as it makes its way around the "segmented" curve. The operator thinks it’s just a machine issue and so dials down the cutting speed. This sends overall cutting capacity downward, and edge quality becomes hit or miss. The problems snowball as the job moves to forming, welding, powder coating, and beyond—all because a (likely overworked) estimator or CAD technician in the office forgot a few mouse clicks.

Senior Editor

Tim Heston

can be reached at

theston@fmamfg.org

.

PEP Technology,

www.peptechnology.com

Need greater Efficiency? MAX it.

Most machine tools can dependably produce parts, but OMAX waterjets make consistency look effortless while shaving minutes from run time. With the superior integration of OMAX’s software, pumps and cutting tables, efficiency is no longer out of reach.

Visit

OMAX.com

and

MAX it

.

XPR

®

plasma pays you back

Power Your Profitability.

Hypertherm XPR

®

plasma pays you back with maximum versatility, productivity, and precision.

Discover how XPR plasma pays you back: