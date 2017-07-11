{% extends "layout.html.tpl" %}
{% block title %}
    Appier - Error
{% endblock %}
{% block content %}
    <div class="debugger">
        <div class="header">
            <h1>{{ full_name }}</h1>
            <p>{{ code }} - {{ message }}</p>
        </div>
        {% if lines %}
            <div class="traceback">
                {% if extended %}
                    {% for item in extended %}
                        <div class="line">File "{{ item.path }}", line {{ item.lineno }}, in {{ item.context }}
                            {% if item.git_url %}
                                &bull; <a class="image" href="{{ item.git_url }}" target="_blank">{{ item.git_service|default("git", True) }}</a>
                            {% endif %}
                        </div>
                        <a class="line opener" data-id="{{ item.id }}">{{ item.line }}</a>
                        <div class="lines-extra" data-id="{{ item.id }}">
                            {% for line in item.lines %}
                                <div class="line {% if line.is_target %}target{% endif %}">
                                    <span class="lineno">{{ line.lineno }}</span><pre><code class="python text">{{ line.line|nl_to_br|sp_to_nbsp }}</code></pre>
                                </div>
                            {% endfor %}
                        </div>
                    {% endfor %}
                {% else %}
                    {% for line in lines %}
                        <div class="line">{{ line }}</div>
                    {% endfor %}
                {% endif %}
            </div>
        {% endif %}
    </div>
{% endblock %}
