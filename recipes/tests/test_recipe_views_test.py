
from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_corretct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_return_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_not_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No Recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        # criando uma receita para teste
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        # checando se um receita existe
        self.assertIn('Recipe title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_do_load_recipes_is_not_published(self):
        """Test recipe is published false dot show"""
        # criando uma receita para teste

        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'No Recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_category_view_function_is_corretct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'category test'
        # criando uma receita para teste
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # checando se um receita existe
        self.assertIn(needed_title, content)

    def test_recipe_category_template_do_load_recipes_not_published(self):
        """Test recipe is published false dot show"""
        # criando uma receita para teste

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id}))

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_corretct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipes(self):
        needed_title = 'detail test page - it load one recipe'

        # criando uma receita para teste - feature
        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse(
                'recipes:recipe', kwargs={
                    'id': 1
                }
            )
        )
        content = response.content.decode('utf-8')

        # checando se a page detail existe
        self.assertIn(needed_title, content)

    def test_recipe_detail_template_do_load_recipes_not_published(self):
        """Test recipe is published false dot show"""
        # criando uma receita para teste

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id}))

        self.assertEqual(response.status_code, 404)

    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_return_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=<teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;teste&gt;&quot;',
            response.content.decode('utf-8')
        )
