# Can you 3D-print press brake tooling?

[TARİH: 01.09.2025 The Fabricator]

Bending Basics

Yes, you can, but there’s a lot to learn

STEVE BENSON

C

an you 3D-print your press brake tooling? Yes, you can, but there’s a lot more to it than you might think (see

Figure 1

). Until 3D printing came along, we manufactured press brake punches and dies by removing material; we would put a block of steel in a mill, lathe, or similar machine, and start cutting, removing material to find the shape.

With additive manufacturing, you start with nothing and add material to build up the desired shape. And you’re not limited to press brake tooling; perhaps a custom side gauge might be in order. The possibilities are endless.

If you’re just getting into 3D printing, you’ll probably start with a smaller tabletop machine. I have four of those, one of which is a carbon fiber printer that can currently print up to four different colors or material types. These smaller printers have work envelopes large enough to produce your typical segmented press brake tool.

When you hear "3D printing," you might think of fragile plastic models or small prototypes. But today’s additive manufacturing technologies are far more capable.

Fused Deposition Modeling

Standard tabletop systems print using

fused deposition modeling

. FDM is ideal for press brake tooling, soft jaws, and workholding fixtures. It works by using a heated nozzle that extrudes melted thermoplastic filament—like PLA, PETG, ABS, or CF-Nylon—layer by layer onto a build platform.

The printers are widely available and affordable, and they support strong materials, including flexible thermoplastic polyurethane and carbon-reinforced options. You can have custom tools designed and printed in-house, often within just hours. You can also easily reinforce your tooling with embedded metal plates, dowels, or bolts.

FDM isn’t as detailed as resin-based systems, but that’s rarely a concern for press brake tooling anyway. Even so, parts can be anisotropic (more on this later), making them weak across layer lines if they’re improperly printed. Some materials, like ABS, may warp or delaminate if you don’t set up the printer correctly.

Overall, FDM strikes the best balance of cost, speed, strength, and accessibility (see

Figure 2

). With the right filament and design approach, FDM can produce durable dies, bump tools, V-blocks, and protective forming pads.

FIGURE 1

These 3D-printed tools were on display at Cincinnati Incorporated’s booth at RAPID + TCT back in 2018.

Stereolithography

Stereolithography (SLA) is ideal for high-detail parts, models, or molds, but it is not really good for press brake tooling. This method uses a UV laser to cure liquid resin in a vat, forming highly detailed parts one layer at a time. It produces parts with fine surface detail to extremely high resolutions. It’s great for mold masters or cosmetic parts, and you can achieve very tight tolerances.

That said, the material can be brittle and so ill-suited for load-bearing use. SLA-printed parts tend to be too brittle and fragile to survive the loads and impacts of forming operations. They require postprocessing (washing, UV curing), and are often limited to smaller build volumes. It’s not ideal for the shop floor, and it’s not ideal for press brake tooling despite the visual quality.

Selective Laser Sintering

Selective laser sintering

(SLS) produces high-performance parts with complex geometry. A laser sinters powdered polymer (usually Nylon) into solid parts inside a heated chamber. The unused powder supports overhangs. The process requires no support structures, and the resulting parts are strong, isotropic, and have good durability. It’s ideal for producing complex internal structures and moving assemblies.

On the downside, machines and materials used for SLS are expensive, and the resulting part surfaces are rougher than those produced with SLA. SLS is very capable, especially with Nylon 12 or filled powders, but most fab shops won’t have direct access to it. That said, outsourcing SLS parts for special tooling projects is a growing trend.

The Filaments

Hundreds of material types are available as filaments for 3D printers, and more are continually being introduced. These include PLA, PETG, PAU, Nylon, carbon, and glass fibers, as well as ceramics, porcelain, and metals (though many older printers might not be capable of producing with metal).

Many filaments, such as those working with metals, require specialized build plates, extruder heads, and special glue. Most filaments come on 2.2-lb. spools but can also be found in both larger and smaller quantities, as well as several different filament diameters.

When it comes to 3D printing, you need to understand the language of this new craft. Once you have mastered that, everything else is easy.

FIGURE 2

If you’re wanting to print custom tools, go/no-go gauges, gauge fingers, and similar items used in the press brake department, you’ll probably print using the FDM process.

Addressing Misconceptions

Most think 3D-printed tooling has many limitations. They think that plastic simply isn’t strong enough. That’s a misconception. True, some plastics are not strong enough to be used, but the strength of the tool is much more than just the material.

The tool profile, wall thickness, layer thickness, and printing speed all are factors. You also have the infill or matrix pattern you print in the tool’s center—solid is not always the best choice (see

Figure 3

). I’ll be diving deep into this and related topics in future columns, so stay tuned.

Isotropic and Anisotropic

A material is

isotropic

when its mechanical properties are the same in all directions. No matter how you bend, stretch, or load it, it behaves consistently. If you print, bend, or machine an isotropic material, it doesn’t matter which way the grain or layers are oriented; it has uniform strength and stiffness throughout. Metals, such as annealed steel or SLS-printed Nylon, tend to behave isotropically.

An

anisotropic

material has different mechanical properties depending on the direction of the load or stress. Most 3D-printed parts and tools made by FDM are anisotropic. They are usually stronger along the layer lines (X and Y axes) but weaker across layers (Z axis). Most sheet metal also is anisotropic to some extent; grain direction affects bend strength and springback.

New Technology, Big Potential

So, how do you print a tool so that it’s strong enough for the forming process? I’ll dive into details in future columns, but for now, I’ll leave you with an initial tip: When printing with FDM, always orient parts so that the strongest direction (infill and wall flow) aligns with the direction of stress during the forming process.

I realize that I have just brought you a lot of new terminology not directly related to forming sheet metal—but it will be. If you want to be able to 3D-print press brake tooling successfully, you need to learn a lot. Most crucially, you need to understand the language of this new craft. Once you have mastered that, everything else is easy.

Next month, we will look at understanding filaments: strength, durometer, and suitability of the different materials (filaments). Until then …

Vaya con Dios

.

FIGURE 3

A 3D printer creates a part with a honeycomb interior. When it comes to 3D printing, solid isn’t always best.

kynny/iStock/Getty Images Plus

Steve Benson

is a member and former chair of the Precision Sheet Metal Technology Council of the Fabricators and Manufacturers Association. He is the president of ASMA LLC,

steve@theartofpressbrake.com

. Benson also conducts FMA’s Precision Press Brake Certificate Program, which is held at locations across the country. For more information, visit

www.fmamfg.org/training

, or call 888-394-4362. The author’s latest book, "Bending Basics," is now available at the FMA bookstore,

www.fmamfg.org/store

.

Built for Efficiency, Priced for Accessibility. ASTES4 HIGH SPEED SKYWAY.

Compact. Fast. Fully automated from load to next operation.

Compact. Unmanned. Built for throughput. The

ASTES4 High Speed Skyway

is designed for facilities where every square foot, and every second, counts. With high-speed part sorting, unmanned automation, and a compact footprint, the Skyway helps you move more parts faster with less labor. Engineered for high-demand environments, the Skyway optimizes the entire material flow: loading, cutting, sorting, and getting parts to the next operation without manual touchpoints slowing you down. Forget the term "entry-level." This is elite automation for shops that need efficiency without excess. Fast. Scalable. Retrofittable. Ready for tomorrow’s production challenges today.

MC MACHINERY SYSTEMS, INC.

a subsidiary of Mitsubishi Corporation

Scan to automate your workflow today

SEE YOU AT

BOOTH A2123