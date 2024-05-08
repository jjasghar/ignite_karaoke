# Ignite Karaoke
## Scope

This is a helper script to create an Ignite Karaoke in just a couple commands.
What is Ignite Karoke?
```text
This is for fun, FrienDA applies.
It go NSFW, but doesn't have to.
The volunteer has 1 minute.
15 seconds each slide.
A title slide to start it off.
Three slides to cover the other 45 seconds.
```

It's a ton of fun in a presentation place, it's amazing what stories you can create from it.

## Setup

```bash
git clone https://github.com/jjasghar/ignite_karaoke
cd ignite_karaoke
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py --help
```

## Running

After you have a working environment, if you want to you can add more pictures (`.png`) to the [imgs/](./imgs), directory
or let it create the presentation for you.

The following example command will create a three person presentation of JJ, Mary, Jane and open the web browser with the
introduction presentation. All you need to do is add however many volunteers you want. Use `" "` if you want to have full names.
```bash
python main.py -c -n JJ Mary Jane -o
python main.py -c -n "JJ Asghar" "Mary Irwin" "Jane Doe" -o
```

**NOTE**: The volunteer presentations have the 15 second auto advance already, so they just need to be there when they have they "Are you ready slide."

When you are done and need to clean up you can run
```bash
python main.py -d
```

## Future Plans

- Add OpenAI support so _one_ of the pictures is created by OpenAI
- Additional images (PRs Accepted!)

## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2024- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
