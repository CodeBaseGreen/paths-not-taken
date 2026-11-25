---
# Reference library: every paper cited across the posts' PDFs, grouped by topic.
icon: fas fa-book
order: 4
toc: true
---

{% assign lib = site.data.library %}
Every paper cited in the PDFs on this site, in one place: **{{ lib | size }} references** across
{{ site.data.library_topics | size }} topics. Within each topic, entries are listed by first author's surname,
then year. Each shows which posts cite it. A [BibTeX file]({{ '/library.bib' | relative_url }}) of the whole
list can be imported into Zotero, Mendeley or similar.

{% for t in site.data.library_topics %}
{% assign items = lib | where: "topic", t.id | sort: "sort" %}
## {{ t.name }}
<p class="lib-blurb">{{ t.blurb }} <span class="lib-count">{{ items | size }}</span></p>
<ol class="lib-list">
{% for e in items %}<li class="lib-item" id="{{ e.key }}">{% include library-entry.html e=e %}</li>
{% endfor %}</ol>
{% endfor %}

<style>
.lib-blurb{color:var(--text-muted-color,#6b6a63);margin:-.3rem 0 .6rem;font-size:.95rem}
.lib-count{display:inline-block;margin-left:.4rem;padding:0 .45rem;border-radius:.6rem;font-size:.8rem;background:var(--tag-bg,rgba(127,127,127,.12))}
.lib-list{list-style:none;padding-left:0;margin-bottom:2rem}
.lib-item{padding:.45rem 0 .45rem 1.6rem;text-indent:-1.6rem;border-bottom:1px solid var(--main-border-color,rgba(127,127,127,.15));line-height:1.5}
.lib-item:last-child{border-bottom:0}
.lib-cited{font-size:.85rem;color:var(--text-muted-color,#6b6a63)}
.lib-cited a{white-space:nowrap}
</style>
