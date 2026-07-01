# The Ultimate Photo Editing Tool - Made for Instrucables

Source: https://www.instructables.com/The-Ultimate-Photo-Editing-Tool-Made-for-Instrucab/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.png)

![Intro 2](images/intro_02.png)

![Intro 3](images/intro_03.png)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

Clear Cut Photo Editor

This is my dream photo editor I wish I had when I first started publishing Instrcutables!

Instead of waiting around for it to be built by someone else (maybe) - I made it myself!

The photo editor, which I have named Clear Cut, was built to make batch changes on images simple and easy. Primarily — I made it so I could batch process images for Instructables builds. However, it's a great tool to use for individual images as well.

The 2 main highlights in this editor are the background removal and adding shadows to images. Once the background has been removed, you can pick the colour you want or have it transparent.

There are multiple controls to help with adjusting the image so it looks just right. Again, these are simple to use and you can also add a preset to your favourite adjustments to use in other editing projects.

I've kept the tools to a minimum and have made a concerted effort not to include any controls that just waste space or are hardly ever used.


## Supplies

![Supplies image 1](images/step01_01.png)

![Supplies image 2](images/step01_02.png)

Everything you need is free and runs entirely in your browser — no installs, no sign up, nothing to download.

- A modern web browser (Chrome recommended)

- Your photos (JPG, PNG, or WebP)

- That's it!

Open the editor here:[https://lonesoulsurfer.github.io/clear-cut-photo-editor/](https://lonesoulsurfer.github.io/clear-cut-photo-editor/)

Full source code and documentation available on GitHub:[https://github.com/lonesoulsurfer/clear-cut-photo-editor](https://github.com/lonesoulsurfer/clear-cut-photo-editor)


## Step 1: Starting a Session

![Step 1: Starting a Session image 1](images/step02_01.png)

![Step 1: Starting a Session image 2](images/step02_02.png)

STEP 1

When you open the editor you'll be prompted to start a new session or resume a previous one.

1. New session — starts fresh with a clean workspace. Give it a name or leave the default (auto-named by date)
2. Resume — picks up where you left off, including the folder you were working from
3. Click "Choose Photos folder & start" to select your working folder and begin
4. Files are saved to Photos / [session name] / inside the folder you choose.
5. You'll then enter the photo editor screen


## Step 2: Loading Images to the Editor

![Step 2: Loading Images to the Editor image 1](images/step03_01.png)

![Step 2: Loading Images to the Editor image 2](images/step03_02.png)

![Step 2: Loading Images to the Editor image 3](images/step03_03.jpg)

STEPS

1. Click or drag photos directly onto the drop zone in the preview area. Supports JPG, PNG, and WebP. You can load multiple images at once.
2. Once loaded, images appear in the filmstrip at the bottom of the preview. Click any thumbnail to switch to it. Hover a thumbnail to reveal the X remove button.
3. You can move through the filmstrip by either using the arrow keys on your keyboard or use your mouse and click on the arrow symbols on either side of the image

Tip: When you add new images, any slider adjustments you've already made are automatically inherited by the new images.


## Step 3: Adjustment Controls

![Step 3: Adjustment Controls image 1](images/step04_01.png)

![Step 3: Adjustment Controls image 2](images/step04_02.png)

STEPS:

The right panel contains all tone and colour controls.

1. Brightness — Overall exposure. Push up to lift the image, pull down to darken.
2. Contrast — Separation between lights and darks.
3. Sharpness — Edge crispness. Useful for product shots.
4. Colour — Saturation. Pull left to desaturate, push right to boost.
5. Warmth — Colour temperature. Orange/warm vs blue/cool.
6. Highlights — Recover blown highlights or push them brighter.
7. Shadows — Lift or crush the shadow areas independently.
8. All sliders default to 0. The value badge turns accent-coloured when a slider is active.

ROTATION & STRAIGHTEN

1. Below the sliders, four buttons handle 90° rotation (CCW, CW, 180°, reset to 0°). The Straighten slider fine-tunes tilt from -45° to +45°.

PRESETS

Save your current slider state as a named preset so you can reuse it across projects.

1. Dial in the adjustments you want
2. Type a name in the preset field and click "+ Save current as preset"
3. Click any saved preset to instantly apply it to the current image
4. Click X on a preset to delete it

Presets are saved to your browser's local storage and persist between sessions.

APPLY TO ALL & RESET

1. Apply adjustments to all — copies the current image's slider settings across every image in the session
2. Reset — zeros out all sliders and rotation for the current image

UNDO / REDO

1. Each image has its own undo/redo history. Use the Undo and Redo buttons above the drop zone.


## Step 4: Mouse Controls

![Step 4: Mouse Controls image 1](images/step05_01.png)

STEP 7:

Use your mouse to navigate, zoom, and crop within the preview area. This is how you enlarge/reduce the size of the image and also centre it

1. Zoom in / out — Scroll wheel over the preview
2. Pan — Right-click and drag
3. Freehand crop — Left-click and drag to draw a crop region
4. Zoom to selection — Left-drag then release — the canvas zooms to fit your selection
5. Next / Prev image — Hover the left or right edge of the preview for arrow navigation

Tip: When in freehand selection mode, the canvas ratio tooltip at the bottom shows the pixel dimensions of your selection as you drag. Release to confirm the crop.


## Step 5: Removing the Background

![Step 5: Removing the Background image 1](images/step06_01.jpg)

![Step 5: Removing the Background image 2](images/step06_02.png)

![Step 5: Removing the Background image 3](images/step06_03.png)

STEPS:

Before you commit and save a colour background, you can do a preview. The default colour is white but you can change this to any of the colours you want once the preview has beenprocessed

1. Choose what background to place behind a subject after background removal.
2. Pick from the preset swatches (including transparent), or click the + tile to choose a custom colour. The label below the swatches shows your current selection.

Options include:

1. Transparent (exports as PNG with no background)
2. White, light grey, mid grey, black
3. A range of colours including red, amber, yellow, lime, teal, sky, navy, purple, and forest green
4. Custom colour — click the + swatch and use the colour picker to choose any colour you like

See a preview

1. Hit the preview button
2. you will need to wait about 15 seconds for the background to be removed
3. Hit the 'Preview BG on all images' to add the background removal on all of the film stack images you have added.


## Step 6: Adding a Shadow Effect

![Step 6: Adding a Shadow Effect image 1](images/step07_01.jpg)

![Step 6: Adding a Shadow Effect image 2](images/step07_02.png)

![Step 6: Adding a Shadow Effect image 3](images/step07_03.png)

![Step 6: Adding a Shadow Effect image 4](images/step07_04.png)

STEPS:

After background removal, the Shadow panel lets you add a realistic drop shadow to your subject.

1. enable the shadow application
2. You will see a shadow appear instantly under the image. This now can be adjusted to suit the image by using the controls

Controls

1. Drag the angle dial to set the direction the light is coming from
2. Use the sliders to refine the look:
3. Strength — Opacity of the shadoW
4. Softness — How blurred/feathered the edges are
5. Spread — How far the shadow extends outward
6. Width — Horizontal scale of the shadow
7. Distance — How far the shadow is offset from the subject
8. Click "Disabled" to toggle the shadow on or off

Applying Shadows to the Other Images

1. Once you're happy with the shadow,uou can click "Apply background & shadow to all" to push these settings across every image in the session.
2. However you don't have to do this and can add a shadow to each image individually if you like
3. If you do apply to all and don't like the look of a particular shadow, then you can use the controls to adjust or just turn of shadow for that particular image


## Step 7: Collage Images

![Step 7: Collage Images image 1](images/step08_01.png)

![Step 7: Collage Images image 2](images/step08_02.png)

![Step 7: Collage Images image 3](images/step08_03.jpg)

![Step 7: Collage Images image 4](images/step08_04.jpg)

STEPS:

Switch to Collage mode by clicking the Collage tab at the top of the screen. Your loaded images stay available in the filmstrip at the bottom.

Choosing a Layout

1. The left panel shows a grid of layout options — click any icon to select it
2. Use the Gap slider to set the spacing between images in pixels. The colour you pick will also create a frame around the saved images.
3. Choose a gap colour using the White / Black / Grey buttons — this is the colour shown between and around your images

Assigning Images to Slots

1. Click a slot in the canvas to select it — it will highlight with a coloured border
2. The filmstrip thumbnails at the bottom will glow to show they are ready to assign
3. Click any thumbnail in the filmstrip to assign that image to the selected slot
4. Repeat for each slot in the layout
5. Once assigned, scroll to zoom and right-drag to pan within each slot to frame the image exactly how you want it

Adjusting Each Image

1. The adjustments work exactly the same as when in editor mode. same with removing backgrounds, adding shadows etc.

Saving

1. Click Save collage to export the full layout as a single image
2. If you want to keep the original backgrounds on all images, click Save collage (keep all BGs) instead — all adjustments are applied but no background removal is run
3. If any slot uses a transparent background, the collage will automatically export as PNG to preserve the transparency

Starting Over

1. Click Start over (keep images) at the bottom of the left panel to clear all slot assignments, adjustments, background removals and shadows
2. Your filmstrip images stay loaded and ready to re-assign to a fresh layout
3. To reset a single slot only, select it and click Reset


## Step 8: Export & Output

![Step 8: Export & Output image 1](images/step09_01.png)

![Step 8: Export & Output image 2](images/step09_02.png)

STEPS:

The right panel controls canvas size and export resolution.

CANVAS

Choose the output aspect ratio for your image:

1. Original — keeps the image's native dimensions
2. Landscape 3:2 — standard landscape crop
3. Portrait 2:3 — standard portrait crop
4. Square 1:1 — square crop, great for product listings
5. Fit to canvas — fits the image within the canvas without cropping
6. Freehand selection — drag on the preview to define a custom crop region

EXPORT SIZE

1. Set the output resolution at 100%, 75%, 50%, or 25% of the canvas size. Use a lower percentage to reduce file size for web use.
2. If you are publishing to Instrcutables and used your photo to take images, then I would suggest reducing the size down to 75%


## Step 9: Saving Your Images to a Folder

![Step 9: Saving Your Images to a Folder image 1](images/step10_01.jpg)

![Step 9: Saving Your Images to a Folder image 2](images/step10_02.png)

![Step 9: Saving Your Images to a Folder image 3](images/step10_03.png)

![Step 9: Saving Your Images to a Folder image 4](images/step10_04.jpg)

SAVING

When you're happy with your edits, save your image using the buttons at the bottom of the right panel.

1. Save this photo + Remove BG — exports the current image with all adjustments and background removal applied
2. Save all photos — batch exports every image in the filmstrip. A progress bar tracks the queue so you can see how it's going.

Exports are saved directly to your session folder. If background removal was applied, images export as PNG to preserve transparency — unless you chose a solid background colour, in which case they export as JPG.


---
*32 images archived*
