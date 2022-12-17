# Generated by Django 3.2.11 on 2022-04-08 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentForPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('user_name', models.CharField(blank=True, max_length=40)),
                ('category_id', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TempMyShortCutForBackEnd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content1', models.CharField(blank=True, max_length=180)),
                ('content2', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wm.category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wm.type')),
            ],
        ),
        migrations.CreateModel(
            name='TempMyShortCut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content1', models.CharField(blank=True, max_length=180)),
                ('content2', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wm.category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wm.type')),
            ],
        ),
        migrations.CreateModel(
            name='RecommandationUserAboutSkillNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyShortCut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('filename', models.CharField(blank=True, max_length=120)),
                ('content1', models.CharField(blank=True, max_length=180)),
                ('content2', models.TextField(blank=True)),
                ('created', models.DateTimeField()),
                ('page_user', models.CharField(blank=True, max_length=20, null=True)),
                ('team_member', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='wm/%y%m%d')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wm.category')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wm.type')),
            ],
        ),
        migrations.CreateModel(
            name='MyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_content', models.CharField(max_length=120)),
                ('completed', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('start_ca', models.CharField(default='ca1', max_length=30)),
                ('end_ca', models.CharField(default='ca1', max_length=30)),
                ('owner_for_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeGuestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LectureBookMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('lecture_url', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommonSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentForShortCut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shortcut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wm.myshortcut')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryNick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca_subtitle', models.CharField(default='my category info', max_length=50)),
                ('ca1', models.CharField(default='ca1', max_length=50)),
                ('ca2', models.CharField(default='ca2', max_length=50)),
                ('ca3', models.CharField(default='ca3', max_length=50)),
                ('ca4', models.CharField(default='ca4', max_length=50)),
                ('ca5', models.CharField(default='ca5', max_length=50)),
                ('ca6', models.CharField(default='ca6', max_length=50)),
                ('ca7', models.CharField(default='ca7', max_length=50)),
                ('ca8', models.CharField(default='ca8', max_length=50)),
                ('ca9', models.CharField(default='ca9', max_length=50)),
                ('ca10', models.CharField(default='ca10', max_length=50)),
                ('ca11', models.CharField(default='ca11', max_length=50)),
                ('ca12', models.CharField(default='ca12', max_length=50)),
                ('ca13', models.CharField(default='ca13', max_length=50)),
                ('ca14', models.CharField(default='ca14', max_length=50)),
                ('ca15', models.CharField(default='ca15', max_length=50)),
                ('ca16', models.CharField(default='ca16', max_length=50)),
                ('ca17', models.CharField(default='ca17', max_length=50)),
                ('ca18', models.CharField(default='ca18', max_length=50)),
                ('ca19', models.CharField(default='ca19', max_length=50)),
                ('ca20', models.CharField(default='ca20', max_length=50)),
                ('ca21', models.CharField(default='ca21', max_length=50)),
                ('ca22', models.CharField(default='ca22', max_length=50)),
                ('ca23', models.CharField(default='ca23', max_length=50)),
                ('ca24', models.CharField(default='ca24', max_length=50)),
                ('ca25', models.CharField(default='ca25', max_length=50)),
                ('ca26', models.CharField(default='ca26', max_length=50)),
                ('ca27', models.CharField(default='ca27', max_length=50)),
                ('ca28', models.CharField(default='ca28', max_length=50)),
                ('ca29', models.CharField(default='ca29', max_length=50)),
                ('ca30', models.CharField(default='ca30', max_length=50)),
                ('ca31', models.CharField(default='ca31', max_length=50)),
                ('ca32', models.CharField(default='ca32', max_length=50)),
                ('ca33', models.CharField(default='ca33', max_length=50)),
                ('ca34', models.CharField(default='ca34', max_length=50)),
                ('ca35', models.CharField(default='ca35', max_length=50)),
                ('ca36', models.CharField(default='ca36', max_length=50)),
                ('ca37', models.CharField(default='ca37', max_length=50)),
                ('ca38', models.CharField(default='ca38', max_length=50)),
                ('ca39', models.CharField(default='ca39', max_length=50)),
                ('ca40', models.CharField(default='ca40', max_length=50)),
                ('ca41', models.CharField(default='ca41', max_length=50)),
                ('ca42', models.CharField(default='ca42', max_length=50)),
                ('ca43', models.CharField(default='ca43', max_length=50)),
                ('ca44', models.CharField(default='ca44', max_length=50)),
                ('ca45', models.CharField(default='ca45', max_length=50)),
                ('ca46', models.CharField(default='ca46', max_length=50)),
                ('ca47', models.CharField(default='ca47', max_length=50)),
                ('ca48', models.CharField(default='ca48', max_length=50)),
                ('ca49', models.CharField(default='ca49', max_length=50)),
                ('ca50', models.CharField(default='ca50', max_length=50)),
                ('ca51', models.CharField(default='ca51', max_length=50)),
                ('ca52', models.CharField(default='ca52', max_length=50)),
                ('ca53', models.CharField(default='ca53', max_length=50)),
                ('ca54', models.CharField(default='ca54', max_length=50)),
                ('ca55', models.CharField(default='ca55', max_length=50)),
                ('ca56', models.CharField(default='ca56', max_length=50)),
                ('ca57', models.CharField(default='ca57', max_length=50)),
                ('ca58', models.CharField(default='ca58', max_length=50)),
                ('ca59', models.CharField(default='ca59', max_length=50)),
                ('ca60', models.CharField(default='ca60', max_length=50)),
                ('ca61', models.CharField(default='ca61', max_length=50)),
                ('ca62', models.CharField(default='ca62', max_length=50)),
                ('ca63', models.CharField(default='ca63', max_length=50)),
                ('ca64', models.CharField(default='ca64', max_length=50)),
                ('ca65', models.CharField(default='ca65', max_length=50)),
                ('ca66', models.CharField(default='ca66', max_length=50)),
                ('ca67', models.CharField(default='ca67', max_length=50)),
                ('ca68', models.CharField(default='ca68', max_length=50)),
                ('ca69', models.CharField(default='ca69', max_length=50)),
                ('ca70', models.CharField(default='ca70', max_length=50)),
                ('ca71', models.CharField(default='ca71', max_length=50)),
                ('ca72', models.CharField(default='ca72', max_length=50)),
                ('ca73', models.CharField(default='ca73', max_length=50)),
                ('ca74', models.CharField(default='ca74', max_length=50)),
                ('ca75', models.CharField(default='ca75', max_length=50)),
                ('ca76', models.CharField(default='ca76', max_length=50)),
                ('ca77', models.CharField(default='ca77', max_length=50)),
                ('ca78', models.CharField(default='ca78', max_length=50)),
                ('ca79', models.CharField(default='ca79', max_length=50)),
                ('ca80', models.CharField(default='ca80', max_length=50)),
                ('ca81', models.CharField(default='ca81', max_length=50)),
                ('ca82', models.CharField(default='ca82', max_length=50)),
                ('ca83', models.CharField(default='ca83', max_length=50)),
                ('ca84', models.CharField(default='ca84', max_length=50)),
                ('ca85', models.CharField(default='ca85', max_length=50)),
                ('ca86', models.CharField(default='ca86', max_length=50)),
                ('ca87', models.CharField(default='ca87', max_length=50)),
                ('ca88', models.CharField(default='ca88', max_length=50)),
                ('ca89', models.CharField(default='ca89', max_length=50)),
                ('ca90', models.CharField(default='ca90', max_length=50)),
                ('ca91', models.CharField(default='ca91', max_length=50)),
                ('ca92', models.CharField(default='ca92', max_length=50)),
                ('ca93', models.CharField(default='ca93', max_length=50)),
                ('ca94', models.CharField(default='ca94', max_length=50)),
                ('ca95', models.CharField(default='ca95', max_length=50)),
                ('ca96', models.CharField(default='ca96', max_length=50)),
                ('ca97', models.CharField(default='ca97', max_length=50)),
                ('ca98', models.CharField(default='ca98', max_length=50)),
                ('ca99', models.CharField(default='ca99', max_length=50)),
                ('ca100', models.CharField(default='ca100', max_length=50)),
                ('ca101', models.CharField(default='ca101', max_length=50)),
                ('ca102', models.CharField(default='ca102', max_length=50)),
                ('ca103', models.CharField(default='ca103', max_length=50)),
                ('ca104', models.CharField(default='ca104', max_length=50)),
                ('ca105', models.CharField(default='ca105', max_length=50)),
                ('ca106', models.CharField(default='ca106', max_length=50)),
                ('ca107', models.CharField(default='ca107', max_length=50)),
                ('ca108', models.CharField(default='ca108', max_length=50)),
                ('ca109', models.CharField(default='ca109', max_length=50)),
                ('ca110', models.CharField(default='ca110', max_length=50)),
                ('ca111', models.CharField(default='ca111', max_length=50)),
                ('ca112', models.CharField(default='ca112', max_length=50)),
                ('ca113', models.CharField(default='ca113', max_length=50)),
                ('ca114', models.CharField(default='ca114', max_length=50)),
                ('ca115', models.CharField(default='ca115', max_length=50)),
                ('ca116', models.CharField(default='ca116', max_length=50)),
                ('ca117', models.CharField(default='ca117', max_length=50)),
                ('ca118', models.CharField(default='ca118', max_length=50)),
                ('ca119', models.CharField(default='ca119', max_length=50)),
                ('ca120', models.CharField(default='ca120', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllowListForSkilNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=30)),
                ('role', models.CharField(blank=True, max_length=10)),
                ('permission', models.BooleanField(default=False)),
                ('start_at', models.IntegerField(blank=True, default=1)),
                ('end_at', models.IntegerField(blank=True, default=1)),
                ('task', models.CharField(blank=True, max_length=30)),
                ('message', models.CharField(blank=True, max_length=30)),
                ('color', models.CharField(blank=True, max_length=10)),
                ('note_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
