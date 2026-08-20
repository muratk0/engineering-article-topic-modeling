# Shop technology and 3-D CAD: Tools for proofreading

[TARİH: 01.07.2014 The Fabricator]

PRECISION MATTERS

For the benefit of better communication of the design, eliminate simple errors

By Gerald Davis, Contributing Writer

Gerald Davis is a job shop consultant and chairman of the board of DSM Manufacturing Co.,

gerald@glddesigns.com

.

In a time when typewriters and drafting boards were state-of-the-art, proofreading could be accomplished only with the labor of another human. Software advancements, however, have replaced both of those antiquities with text editors and CAD systems.

Many text editors and most word-processing systems have grammar and spelling tools. Meanwhile, some mainstream 3-D CAD systems have analogous tools that serve as

design checkers

. Specifically, the 3-D CAD software used in support of preparing this article features a tool called Design Checker. The check-box setting to enable this add-in is shown in Figure 1. Design Checker can be used as a spelling checker, but it has the wits to be much more useful to a CAD jockey.

Figure 1 Design Checker is an add-in and must be enabled prior to use. From the menu bar click on Tools->Add-Ins>Design Checker.

From personal experience I can tell you that the spelling and grammar tools built into the word processor do not improve the substance of what is written. Rather, such proofreading tools prune away the distractions that might be obscuring the brilliance of the prose. Similarly, Design Checker can be a useful tool to identify and to minimize the nuisance of complying with a variety of standards—from spelling to ANSI/ISO. However, it does not check the function of the modeled invention.

Muses (our own euphemism for that which is the purpose of the design effort) are still needed to inspire both the invention as well as how best to evaluate the virtual prototype. We recommend delegating the mundane proofreading to Design Checker and thus enabling the CAD jockey to spend more quality time with the muses.

Figure 3a To make a rule, click on Tools>Design Checker>Build Checks.

Suppose that someone is not able or is unwilling to use a gizmo like Design Checker. That is not a problem. Simply use the antiquated buddy-check proofreading of yore, or worse, rely upon yourself to not make typos. This manual method of proofing—opening the CAD document and scrolling through myriad document properties to perform data entry to control the fonts, arrow sizes, and other standardized settings—can lead to problems, of course. Note in Figure 2 that at least one custom property is mismatched between the drawing template and the component shown in the drawing. Design Checker can be taught to report on all such missing properties to spare the human the effort of mind-numbing searching.

Under the Hood

Design Checker compares the current document, which could be a drawing, a 3-D part, or an assembly of such parts, to a selected standards document. It doesn’t take much time or effort to build a custom standards file. (Keep in mind that the standards document must exist

prior

to checking the design document with Design Checker.)

As a step-by-step demonstration of creating and using a rule to check spelling on a drawing, follow Figures 3a through 4c:

Figure 2 The 2-D sheet format for this drawing is reporting errors: missing custom properties in the 3-D model. You easily can create rules to report on all missing custom properties. You perform the correction and Design Checker just reports.

1. Click on Tools>Design Checker>Build Checks as shown in Figure 3a. This will launch the control panel for Design Checker.

2. Click on Create a New Standards File as shown in Figure 3b. The control panel now shows one of seven tabs on the left. The main screen is blank but will eventually show all of the rules defined in this standards file.

Figure 3b Then click on Create a New Standards File.

3. The Document Checks tab is active by default and lists the checks that are available for documents in general. We need to select the Annotation Checks tab to find the rule for spelling. The fourth one down is Spell Checker as shown in Figure 3c. Click on Spell Checker to enable this rule; click again to disable it if you have a change of heart. We want it enabled.

Figure 3c The Spell Checker rule is on the Annotation Checks tab and is the fourth entry in the rules list. Clicking on the Spell Checker button toggles the rule on/off.

4. Click on File>Save As to save the new standards file. We named ours FMA Spell Checker, but any meaningful name will do. (For the moment, we’re done with using the Design Checker control panel; either close it or just switch back to the graphics window that is displaying the problem drawing.)

5. On the main menu bar, click on Tools>Design Checker>Check Active Document to start applying the rules (see Figure 4a).

Figure 4a To use the new standards rule file, click on Tools>Design Checker>Check Active Document.

6. The Design Checker’s task pane appears and shows a list of available/active standards files to apply as shown in Figure 4b. You may add standards files to the list by clicking on the green “+” and browsing.

Figure 4b Then enable one or more rules to apply to the current document. In this example we are running only the spell check rule. Other rules could be selected for simultaneous processing. A click on the Check Document button will start the checking cycle.

7. In Figure 4b, the FMA Spell Checker standard created in Step 4 has been added to the list and selected to enable the rules it contains. Click on the Check Document button to start checking the spelling in this document against the FMA standard.

8. After a few moments the results of the check are displayed. In Figure 4c the error report is on the right and the model/drawing is shown on the left. Each entry in the error report corresponds to an annotation somewhere on the drawing that has a spelling problem. When the line item on the report is selected with the mouse, the corresponding annotation is magnified on the drawing. In Figure 4c we see that “Featherstone” is missing an “h.” Spelling errors require human intervention for correction.

Figure 4c Click on the “+” to expand the error report details. Mouse clicking on a line in the report will highlight the problem in the graphics window. This makes it easy to find and edit the annotation with bad spelling.

We’ve drawn on the similarity between CAD proofreading tools and spelling checkers. The reporting capabilities of Design Checker go beyond spelling and can be used to auto-correct some features of an archive of old CAD into good compliance with current standards. In situations where several CAD documents require the identical proofreading and corrective treatment, a combination of Task Scheduler and Design Checker can be used to process multiple documents in a folder.

We recommend improving your document templates with Design Checker, as well as using it to check production work. Templates are a frequent source of things that need to be retyped. By cleaning them up, you make Design Checker’s job easier.

Persisting Nuisance

Repetitive tasks sneak their way into the CAD work flow—changing the street name from “Feater-stone” to “Featherstone,” for example. Correcting such an error is a simple task. The problem persists because it is perceived to take more time to correct the template, or whatever source of the problem, than it does to just enter the corrected information each time a drawing is created. If you do it often enough to never forget to do it, then you’re probably wasting time by not correcting the source of the problem.

Avoiding repetitive typing is not the only reason to use Design Checker as part of the routine work flow. Perhaps you work in a job shop that is producing shop drawings from customer-supplied models. Organizational mergers sometimes require documents to be revised to comply with new internal standards. Making Design Checker a part of your regular CAD work flow will brighten your smile and improve relations with collaborators.

You might find it convenient to establish a library of standards, each with a specific proofreading assignment. It is easy to select more than one standard for simultaneous scanning of the current document. But processing time, detection of irrelevant errors, and scope of responsibility are just some of the reasons not to apply all possible checks to each document.

Design Checker makes it convenient to select which combination of your standards to apply during an evaluation. If computer time is an issue, using specific and targeted standards might be a timesaver. On the other hand, if consistency is the most important result, it might be better to simplify the work flow. Put all design checks into a single standards file and use it to check all documents. In that situation, the challenge boils down to remembering to use Design Checker before every document is declared done.

Using Design Checker to detect sketches that are not fully defined is so much easier than scanning an assembly by eyeball. Have you ever released a drawing with a missing datum for a GTOL callout? Design Checker to the rescue!

Gerald Davis uses CAD software to design and develop products for his clients at

www.glddesigns.com

.

He is a former owner and operator of a job shop from 1984 to 2004.

Gerald would love for you to send him your comments and questions. You are not alone, and the problems you face often are shared by others. Share the grief, and perhaps we will all share in the joy of finding answers. Please send your questions and comments to

dand@thefabricator.com

.