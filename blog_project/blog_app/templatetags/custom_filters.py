from django import template
import re

register = template.Library()


@register.filter
def remove_html_tags(value):
    # <p> 태그 내부의 내용을 추출하는 필터
    pattern = r"<p>(.*?)<\/p>"
    result = re.findall(pattern, value)
    result = [re.sub(r"&nbsp;", "", item.strip()) for item in result]
    result = [re.sub(r"<img[^>]*>", "", item) for item in result]
    return " ".join(result)

@register.filter
def extract_first_image_tag(text):
    pattern = re.compile(r'<img[^>]*src=["\'](.*?)["\']')
    matches = pattern.findall(text)
    
    if matches:
        return matches[0]
    
    return ""