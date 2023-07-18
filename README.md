## What is This?
A personal project I'm playing around with. Trans people are often tasked with choosing a new name for themselves, and that can be hard! I wanted to create a way we can easily swipe through different names until we find one that fits. Yes, this could also be used for baby naming.

I have so many big ideas for this project, that it will certainly be in versioned.

## Plans!

- Flask Backend with SQLalchemy db
- Next.js + TS + React front end + Redux store
- Prob don't need caching? since there's not much page nav.
- Why did I choose these? because I like TS and I haven't done much python in 3 years.

#### mvp/v0
- Swiping through index cards and adding ones to a single list that you like
- Adding user sign up/log in

#### v1 + beyond
- Adding different descriptors to names (theme, origin, pronunciation, meaning, etc).
- Use these descriptors to vectorize to add a "view similar names to this one" button (aka use NLP)
- Allow users to create different lists (besides yesses/nos) (account for this in initial construction)
- Figure out additional data aggregation (allow user submitted names? add security to this?)
- ...tbd

## Intended Design

| Landing Page           | Open Drawer               |
| ---------------------- | ---------------------- |
| ![1](https://github.com/julwhitney13/rename-me/assets/8354632/43bde3c0-766d-4ce5-bc22-dc07cefdded8) | ![2](https://github.com/julwhitney13/rename-me/assets/8354632/e1ee28a3-760d-4374-8268-82bc3e28441d)|


## Intended MVCs

<img src="https://github.com/julwhitney13/rename-me/assets/8354632/89e6201e-e459-4ce2-a9da-9ddb55c96842" width="500"/>



## Getting Started

Currently a WIP... but I'll remove this when I'm ready, so:

To run FE:

```bash
npm i
npm run dev
```

To run BE:
```bash
source .venv/bin/activate
pip install -r api/requirements.txt
flask run
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

